from . import bp

@bp.route('/', methods=['GET', 'POST'])
def test():
    return "Hello World"