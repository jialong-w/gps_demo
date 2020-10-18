"""Console script for gps_demo."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for gps_demo."""
    click.echo("Replace this message by putting your code into "
               "gps_demo.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
