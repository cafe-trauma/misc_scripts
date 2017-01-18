import requests
import glob

def run_statements(data, context):
    headers = {'content-type': 'application/rdf+xml'}
    params = {'context': '<file://{}>'.format(context)}
    r = requests.request('DELETE',
                         'http://dev.cafe-trauma.com/rdf/statements',
                         params=params)
    if(r.ok):
        print('delete: {}'.format(context))
    else:
        print(r.text)
    r = requests.request('POST',
                         'http://dev.cafe-trauma.com/rdf/statements',
                         data=data, headers=headers, params=params)
    if(not r.ok):
        print(r.text)
    else:
        print('finished: {}'.format(context))
        print('len: {}'.format(len(data)))

for filename in glob.glob('*.owl'):
    with open(filename) as f:
        run_statements(f.read(), filename)
