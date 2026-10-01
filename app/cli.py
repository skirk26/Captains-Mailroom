import click
from flask.cli import with_appcontext

from app import db
from app.models import Staff


@click.command("create-staff")
@click.argument("username")
@click.password_option()
@with_appcontext
def create_staff(username, password):
    """Create a mailroom staff account."""
    if db.session.scalar(db.select(Staff).filter_by(username=username)):
        raise click.ClickException(f"Staff user '{username}' already exists.")

    staff = Staff(username=username)
    staff.set_password(password)
    db.session.add(staff)
    db.session.commit()
    click.echo(f"Created staff user '{username}'.")
