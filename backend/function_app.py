import azure.functions as func
from auth.register import __init__ as register
from auth.login import __init__ as login
from auth.logout import __init__ as logout
from users.get_profile import __init__ as get_profile
from users.update_profile import __init__ as update_profile
from users.update_pref import __init__ as update_pref
from users.delete_account import __init__ as delete_account
from admin.get_all_users import __init__ as get_all_users
from admin.block_user import __init__ as block_user
from admin.change_role import __init__ as change_role
from admin.reset_password import __init__ as reset_password
from admin.get_reports import __init__ as get_reports
from pokemon.get_pokemon import __init__ as get_pokemon
from pokemon.search_pokemon import __init__ as search_pokemon
from favorites.get_favorites import __init__ as get_favorites
from favorites.add_favorites import __init__ as add_favorites
from favorites.remove_favorites import __init__ as remove_favorites
from team.get_team import __init__ as get_team
from team.add_to_team import __init__ as add_to_team
from team.remove_from_team import __init__ as remove_from_team
from team.update_team import __init__ as update_team

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="auth/register", methods=["POST"])
def auth_register(req: func.HttpRequest) -> func.HttpResponse:
    return register.main(req)

@app.route(route="auth/login", methods=["POST"])
def auth_login(req: func.HttpRequest) -> func.HttpResponse:
    return login.main(req)

@app.route(route="auth/logout", methods=["POST"])
def auth_logout(req: func.HttpRequest) -> func.HttpResponse:
    return logout.main(req)

@app.route(route="users/profile", methods=["GET"])
def users_get_profile(req: func.HttpRequest) -> func.HttpResponse:
    return get_profile.main(req)

@app.route(route="users/profile", methods=["PUT"])
def users_update_profile(req: func.HttpRequest) -> func.HttpResponse:
    return update_profile.main(req)

@app.route(route="users/preferences", methods=["PUT"])
def users_update_pref(req: func.HttpRequest) -> func.HttpResponse:
    return update_pref.main(req)

@app.route(route="users/account", methods=["DELETE"])
def users_delete_account(req: func.HttpRequest) -> func.HttpResponse:
    return delete_account.main(req)

@app.route(route="mgmt/users", methods=["GET"])
def admin_get_all_users(req: func.HttpRequest) -> func.HttpResponse:
    return get_all_users.main(req)

@app.route(route="mgmt/block", methods=["PUT"])
def admin_block_user(req: func.HttpRequest) -> func.HttpResponse:
    return block_user.main(req)

@app.route(route="mgmt/role", methods=["PUT"])
def admin_change_role(req: func.HttpRequest) -> func.HttpResponse:
    return change_role.main(req)

@app.route(route="mgmt/reset-password", methods=["PUT"])
def admin_reset_password(req: func.HttpRequest) -> func.HttpResponse:
    return reset_password.main(req)

@app.route(route="mgmt/reports", methods=["GET"])
def admin_get_reports(req: func.HttpRequest) -> func.HttpResponse:
    return get_reports.main(req)

@app.route(route="pokemon/search", methods=["GET"])
def pokemon_search(req: func.HttpRequest) -> func.HttpResponse:
    return search_pokemon.main(req)

@app.route(route="pokemon/{name_or_id}", methods=["GET"])
def pokemon_get(req: func.HttpRequest) -> func.HttpResponse:
    return get_pokemon.main(req)

@app.route(route="favorites", methods=["GET"])
def favorites_get(req: func.HttpRequest) -> func.HttpResponse:
    return get_favorites.main(req)

@app.route(route="favorites", methods=["POST"])
def favorites_add(req: func.HttpRequest) -> func.HttpResponse:
    return add_favorites.main(req)

@app.route(route="favorites/{pokemon_id}", methods=["DELETE"])
def favorites_remove(req: func.HttpRequest) -> func.HttpResponse:
    return remove_favorites.main(req)

@app.route(route="team", methods=["GET"])
def team_get(req: func.HttpRequest) -> func.HttpResponse:
    return get_team.main(req)

@app.route(route="team", methods=["POST"])
def team_add(req: func.HttpRequest) -> func.HttpResponse:
    return add_to_team.main(req)

@app.route(route="team", methods=["PUT"])
def team_update(req: func.HttpRequest) -> func.HttpResponse:
    return update_team.main(req)

@app.route(route="team/{pokemon_id}", methods=["DELETE"])
def team_remove(req: func.HttpRequest) -> func.HttpResponse:
    return remove_from_team.main(req)