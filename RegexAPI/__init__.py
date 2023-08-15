import logging
import json
import re
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('RegexAPI processed a request.')

    req_body = req.get_json()

    content = req_body.get('content')
    pattern = req_body.get('pattern')

    repatter = re.compile(pattern)
    result = repatter.search(content)

    return func.HttpResponse(
        json.dumps({
            'method': req.method,
            'url': req.url,
            'headers': dict(req.headers),
            'params': dict(req.params),
            'content': content,
            'pattern': pattern,
            'result': result.group()
        }),
        mimetype="application/json"
    )