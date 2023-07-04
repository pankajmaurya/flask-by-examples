Flask context processors are functions in Flask that allow you to inject variables or functions into the context of a template. They provide a way to make certain variables or functions available globally to all templates without explicitly passing them in each rendering call.

Context processors are registered using the @app.context_processor decorator in Flask. The decorated function returns a dictionary of values that will be added to the template context. These values can then be accessed directly within templates.

A context processor can also make functions available in the template context.

