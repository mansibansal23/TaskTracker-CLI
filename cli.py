import click
import requests

API_URL = "http://127.0.0.1:8001"

@click.group()
def cli():
    pass

@cli.command()
@click.argument('title')
@click.option('--description', default="", help="Description of the task.")
def add(title, description):
    """Add a new task."""
    response = requests.post(f"{API_URL}/tasks/", params={"title": title, "description": description})
    click.echo(response.json())

@cli.command()
def list():
    """List all tasks."""
    response = requests.get(f"{API_URL}/tasks/")
    tasks = response.json()
    for task in tasks:
        click.echo(f"{task['id']}: {task['title']} [{task['status']}]")

@cli.command()
@click.argument('task_id', type=int)
@click.argument('status', type=click.Choice(['To Do', 'In Progress', 'Done']))
def update(task_id, status):
    """Update the status of a task."""
    response = requests.put(f"{API_URL}/tasks/{task_id}", params={"status": status})
    click.echo(response.json())

@cli.command()
@click.argument('task_id', type=int)
def delete(task_id):
    """Delete a task."""
    response = requests.delete(f"{API_URL}/tasks/{task_id}")
    click.echo(response.json())

if __name__ == "__main__":
    cli()
