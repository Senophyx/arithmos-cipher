import click
from .dictionary import *
import re
from arithmos import __version__


@click.group()
def cli():
    """Welcome to Arithmos Cipher on CLI based!"""
    pass

@click.command()
@click.argument('text', nargs=-1)
def encrypt(text):
    encrypted = []
    for t in text:
        enc = ''.join(encrypt_dict[c] for c in list(t))
        encrypted.append(enc)
    click.echo(" ".join(str(i) for i in encrypted))

@click.command()
@click.argument('cipher', nargs=-1)
def decrypt(cipher):
    decrypted = []
    for ciph in cipher:
        decrypted.append(ciph)
    cipher = " ".join(str(i) for i in decrypted)
    separate = re.findall("\d{2}|\w|.|\d\s|\s+|\d$", cipher)
    click.echo(''.join(decrypt_dict[c] for c in separate))

@click.command()
def version():
    click.echo(__version__)

cli.add_command(encrypt)
cli.add_command(decrypt)
cli.add_command(version)
