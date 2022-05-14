import click
from .dictionary import *
import re
from arithmos import __version__
import requests
import json
from requests import RequestException
import os
import colorgb

try:
	from packaging.version import parse
except ImportError:
	from pip._vendor.packaging.version import parse


def get_pypi_version(package="arithmos-cipher"):
	"""Return version of package on pypi.python.org using json."""
	try:
		url_pattern = 'https://pypi.python.org/pypi/{package}/json'
		req = requests.get(url_pattern.format(package=package))
		version = parse('0')
		if req.status_code == requests.codes.ok:
			j = json.loads(req.text.encode(req.encoding))
			releases = j.get('releases', [])
			for release in releases:
				ver = parse(release)
				if not ver.is_prerelease:
					version = max(version, ver)
		return str(version)
	
	except RequestException:
		return "Connection Error!"


class AliasedGroup(click.Group):
	def get_command(self, ctx, cmd_name):
		try:
			cmd_name = ALIASES[cmd_name].name
		except KeyError:
			pass
		return super().get_command(ctx, cmd_name)

def ignorefunc(original, ignore):
	"""A function to replace ignored characters to noting :v"""
	text = str(original)
	ignore = list(ignore)
	for ch in ignore:
		if ch in text:
			text=text.replace(ch,"")
			
	# I don't know why, but text is not a tuple
	text = text.replace("(", "")
	text = text.replace(")", "")
	text = text.replace(",", "")
	text = text.replace("'", "")
	return text

@click.group(cls=AliasedGroup)
def cli():
	"""
	Welcome to Arithmos Cipher on CLI based!
	
	\b
	Commands:
	- encrypt [text] | Alias : enc
	- decrypt [cipher] | Alias : dec
	- version | Alias : ver
	and more...
	
	Check the CLI documentation for more information.
	https://github.com/LyQuid12/arithmos-cipher/blob/master/cli.md
	"""
	pass

@click.command()
@click.argument('text', nargs=-1)
@click.option('--ignore', '-i', help="Set ignored letters.", multiple=True)
def encrypt(text, ignore):
	"""Encrypting string to cipher."""
	text = ignorefunc(text, ignore)
	encrypted = []
	for t in text:
		try:
			enc = ''.join(encrypt_dict[c] for c in list(t))
			encrypted.append(enc)
		except KeyError as key:
			click.echo(f"{colorgb.fore('ERROR', 'lred')} : {colorgb.fore(key, 'lyellow')} cannot be encrypted.")
	click.echo("".join(str(i) for i in encrypted))
	
@click.command()
@click.argument('cipher', nargs=-1)
@click.option('--ignore', '-i', help="Set ignored number.", multiple=True)
def decrypt(cipher, ignore):
	"""Decrypting cipher to string."""
	cipher = ignorefunc(cipher, ignore)
	
	if len(cipher) % 2 == 0:
		decrypted = []
		for ciph in cipher:
			decrypted.append(ciph)
		try:
			cipher = "".join(str(i) for i in decrypted)
			separate = re.findall("\d{2}|\w|.|\d\s|\s+|\d$", cipher)
			click.echo("".join(decrypt_dict[c] for c in separate))
		except KeyError as key:
			click.echo(f"{colorgb.fore('ERROR', 'lred')} : {colorgb.fore(key, 'lyellow')} cannot be decrypted.")
	else:
		click.echo(f"{colorgb.fore('ERROR', 'lred')} : The string you given cannot be as {colorgb.fore('odd', 'lyellow')}, it must be {colorgb.fore('even', 'lyellow')}.")

@click.command()
@click.option('--more', '-m', help='More version information.', required=False, is_flag=True)
def version(more):
	"""Check your arithmos-cipher version."""
	ver = __version__
	if more:
		local_ver = f"Current arithmos-cipher version : {__version__}\n"
		requests_ver = f"Requests version : {requests.__version__}\n"
		click_ver = f"Click version : {click.__version__}\n"
		colorgb_ver = f"Colorgb version : {colorgb.__version__}\n"
		pypi_ver = f"PyPI latest version (arithmos-cipher) : {get_pypi_version()}"

		ver = local_ver+requests_ver+click_ver+colorgb_ver+pypi_ver
	
	click.echo(ver)


@click.command()
def update():
	"""Update arithmos-cipher packages."""
	os.system("pip install -U arithmos-cipher")

@click.command()
def uninstall():
	"""Uninstall arithmos-cipher packages."""
	os.system("pip uninstall arithmos-cipher")

cli.add_command(encrypt)
cli.add_command(decrypt)
cli.add_command(version)
cli.add_command(update)
cli.add_command(uninstall)


ALIASES = {
	"enc": encrypt,
	"dec": decrypt,
	"ver": version,
	"up": update,
	"del": uninstall
}
