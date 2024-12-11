import os
import click
from pydo import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize DigitalOcean Client
def get_client():
    token = os.getenv("DIGITALOCEAN_API_KEY")
    if not token:
        raise click.ClickException("DIGITALOCEAN_API_KEY is not set in environment variables.")
    return Client(token=token)

# CLI group for organizing commands
@click.group()
def cli():
    """Custom CLI for managing DigitalOcean resources."""
    pass

# List Droplets
@cli.command()
def list_droplets():
    """List all droplets."""
    client = get_client()
    try:
        droplets = client.droplets.list()["droplets"]
        if not droplets:
            click.echo("No droplets found.")
        else:
            for droplet in droplets:
                click.echo(
                    f"ID: {droplet['id']}, Name: {droplet['name']}, IP: {droplet['networks']['v4'][0]['ip_address']}, Region: {droplet['region']['slug']}"
                )
    except Exception as e:
        click.echo(f"Error listing droplets: {e}")

# Create a Droplet
@cli.command()
@click.option("--name", prompt="Droplet name", help="The name of the droplet.")
@click.option("--region", default="nyc3", help="Region to create the droplet (default: nyc3).")
@click.option("--size", default="s-1vcpu-1gb", help="Size of the droplet (default: s-1vcpu-1gb).")
@click.option("--image", default="ubuntu-20-04-x64", help="Image for the droplet (default: Ubuntu 20.04).")
def create_droplet(name, region, size, image):
    """Create a new droplet."""
    client = get_client()
    try:
        response = client.droplets.create(name=name, region=region, size=size, image=image)
        droplet = response["droplet"]
        click.echo(f"Droplet created: ID: {droplet['id']}, Name: {droplet['name']}")
    except Exception as e:
        click.echo(f"Error creating droplet: {e}")

# Delete a Droplet
@cli.command()
@click.option("--droplet-id", prompt="Droplet ID", help="The ID of the droplet to delete.")
def delete_droplet(droplet_id):
    """Delete a droplet by ID."""
    client = get_client()
    try:
        client.droplets.delete(droplet_id=droplet_id)
        click.echo(f"Droplet {droplet_id} deleted successfully.")
    except Exception as e:
        click.echo(f"Error deleting droplet: {e}")

# List SSH Keys
@cli.command()
def list_ssh_keys():
    """List all SSH keys."""
    client = get_client()
    try:
        ssh_keys = client.ssh_keys.list()["ssh_keys"]
        if not ssh_keys:
            click.echo("No SSH keys found.")
        else:
            for key in ssh_keys:
                click.echo(f"ID: {key['id']}, Name: {key['name']}, Fingerprint: {key['fingerprint']}")
    except Exception as e:
        click.echo(f"Error listing SSH keys: {e}")

# Add an SSH Key
@cli.command()
@click.option("--name", prompt="Key name", help="Name of the SSH key.")
@click.option("--public-key", prompt="Public key", help="Public SSH key content.")
def add_ssh_key(name, public_key):
    """Add a new SSH key."""
    client = get_client()
    try:
        response = client.ssh_keys.create(name=name, public_key=public_key)
        click.echo(f"SSH key added: ID: {response['ssh_key']['id']}, Name: {response['ssh_key']['name']}")
    except Exception as e:
        click.echo(f"Error adding SSH key: {e}")

# Main Entry Point
if __name__ == "__main__":
    cli()
