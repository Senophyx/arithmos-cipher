import click
from .dictionary import *
import re
from .utils import get_version
from arithmos import __version__


@click.group()
def cli():
    """Welcome to Arithmos Cipher on CLI based"""
    pass

@click.command()
@click.option("--text", "-t", required=True)
def encrypt(text):
    encrypted =''.join(encrypt_dict[c] for c in list(text))
    click.echo(encrypted)

@click.command()
@click.option("--cipher", "-c", required=True)
def decrypt(cipher):
    separate = re.findall("\d{2}|\w|.|\d\s|\s+|\d$", cipher)
    decrypted = ''.join(decrypt_dict[c] for c in separate)
    click.echo(decrypted)
    

@click.command()
def version():
    click.echo(__version__)

cli.add_command(encrypt)
cli.add_command(decrypt)
cli.add_command(version)
