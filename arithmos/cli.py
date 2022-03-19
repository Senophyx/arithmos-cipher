import click
from .dictionary import *
import re
from arithmos import __version__


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
        enc = ''.join(encrypt_dict[c] for c in list(t))
        encrypted.append(enc)
    click.echo("".join(str(i) for i in encrypted))
    
@click.command()
@click.argument('cipher', nargs=-1)
@click.option('--ignore', '-i', help="Set ignored number.", multiple=True)
def decrypt(cipher, ignore):
    """Decrypting cipher to string."""
    cipher = ignorefunc(cipher, ignore)
    decrypted = []
    for ciph in cipher:
        decrypted.append(ciph)
    cipher = "".join(str(i) for i in decrypted)
    separate = re.findall("\d{2}|\w|.|\d\s|\s+|\d$", cipher)
    click.echo("".join(decrypt_dict[c] for c in separate))

@click.command()
def version():
    """Check your arithmos-cipher version."""
    click.echo(__version__)

cli.add_command(encrypt)
cli.add_command(decrypt)
cli.add_command(version)


ALIASES = {
    "enc": encrypt,
    "dec": decrypt,
    "ver": version
}
