"""
Entrypoint module, in case you use `python -m{{cookiecutter.package_name}}`.


Why does this file exist, and why __main__? For more info, read:

- https://www.python.org/dev/peps/pep-0338/
- https://docs.python.org/2/using/cmdline.html#cmdoption-m
- https://docs.python.org/3/using/cmdline.html#cmdoption-m
"""
{%- if cookiecutter.command_line_interface|lower == 'plain' %}
import sys
{% endif %}
from {{cookiecutter.package_name}}.cli import main

if __name__ == "__main__":
{%- if cookiecutter.command_line_interface|lower == 'click' %}
    main()
{%- else %}
    sys.exit(main())
{%- endif %}
