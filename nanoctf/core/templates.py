# -*- coding: utf-8 -*-
import logging
from flask import session, current_app
import flask
from flask_themes2 import Theme
from jinja2.loaders import FileSystemLoader, BaseLoader, TemplateNotFound

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


#
#   TODO refactor this module
#

def render_template(template, theme=None, **context):
    theme = theme or []
    if not isinstance(theme, (list, tuple)):
        theme = [theme]

    sys_theme = session.get('theme', current_app.config.get('DEFAULT_THEME'))
    if sys_theme:
        theme.append(sys_theme)

    logger.debug("Rendering template")
    logger.debug("theme {} - template {} - context {}".format(
        theme, template, context))

    return render_theme_template(theme, template, **context)


# FIXME This method differs from "flask_themes2" that's why theming didn't work.
def render_theme_template(theme, template_name, _fallback=True, **context):
    """
    This renders a template from the given theme. For example::

        return render_theme_template(g.user.theme, 'index.html', posts=posts)

    If `_fallback` is True and the template does not exist within the theme,
    it will fall back on trying to render the template using the application's
    normal templates. (The "active theme" will still be set, though, so you
    can try to extend or include other templates from the theme.)

    :param theme: Either the identifier of the theme to use, or an actual
                  `Theme` instance.
    :param template_name: The name of the template to render.
    :param _fallback: Whether to fall back to the default
    """

    if not isinstance(theme, (list, tuple)):
        theme = [theme]

    logger.debug("Rendering template")
    logger.debug("theme {} - template {} - fallback {} - context {}".format(
        theme, template_name, _fallback, context))

    if not isinstance(template_name, (list, tuple)):
        template_name = [template_name]

    last = template_name.pop()

    themes = theme

    for name in template_name:
        for theme in themes:
            if isinstance(theme, Theme):
                theme = theme.identifier
            context['_theme'] = theme

            try:
                logger.debug(
                    "trying to render {} in {}".format(name, theme)
                )
                return flask.render_template('_themes/%s/%s' % (theme, name),
                                             **context)
            except TemplateNotFound:
                logger.debug(
                    "{} not found in {}, trying next...".format(name, theme))
                continue

    if _fallback:
        logger.debug("Fallback to app templates folder")
        for name in template_name:
            try:
                logger.debug(
                    "trying to render {} in app templates".format(name))
                return flask.render_template(name, **context)
            except TemplateNotFound:
                logger.debug("{} not found, trying next...".format(name))
                continue

    for theme in themes:
        if isinstance(theme, Theme):
            theme = theme.identifier
        context['_theme'] = theme

        try:
            logger.debug(
                "Trying to load last template {} in {}".format(last, theme))
            return flask.render_template('_themes/%s/%s' % (theme, last),
                                         **context)
        except TemplateNotFound:
            continue

    if _fallback:
        logger.debug(
            "Trying to load last template {} in app templates".format(last))
        return flask.render_template(last, **context)

    logger.debug("Template {} not found".format(last))

    raise
