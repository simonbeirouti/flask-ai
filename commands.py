def cli_commands(app):
    @app.cli.command('hello')
    def say_hello():
        print('Hello')

    @app.cli.command('goodbye')
    def goodbye():
        print('Goodbye')