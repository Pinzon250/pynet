"""
pynet.admin.commands.client
---------------------------
Subcomandos para gestionar el catálogo de clientes registrados en el
backend (Azure Key Vault corporativo).

Cada cliente se almacena como un secreto en el KV corporativo con
nombre 'client-{slug}-config' y valor JSON {vault_url, tenant_id,
client_id, client_secret}.
"""

import typer
from rich.console import Console


client_app = typer.Typer(
    help="Gestionar el catálogo de clientes registrados.",
    no_args_is_help=True,
)
console = Console()


@client_app.command("add")
def client_add():
    """Wizard interactivo para registrar un cliente nuevo en el backend."""
    console.print(
        "[yellow]⚠️  pynet-admin client add: no implementado aún.[/yellow]\n"
        "[dim]Se construirá en el paso 7 (CLI admin).[/dim]"
    )


@client_app.command("list")
def client_list():
    """Lista todos los clientes registrados en el backend."""
    console.print(
        "[yellow]⚠️  pynet-admin client list: no implementado aún.[/yellow]\n"
        "[dim]Se construirá en el paso 7 (CLI admin).[/dim]"
    )


@client_app.command("show")
def client_show(
    slug: str = typer.Argument(..., help="Slug del cliente."),
):
    """Muestra los datos de un cliente (con la sensible enmascarada)."""
    console.print(
        f"[yellow]⚠️  pynet-admin client show '{slug}': no implementado aún.[/yellow]"
    )


@client_app.command("remove")
def client_remove(
    slug: str = typer.Argument(..., help="Slug del cliente a eliminar."),
):
    """Elimina un cliente del backend."""
    console.print(
        f"[yellow]⚠️  pynet-admin client remove '{slug}': no implementado aún.[/yellow]"
    )
