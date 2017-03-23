#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import getpass
import requests
import optparse
import foursquare
from bs4 import BeautifulSoup as BS

parser = optparse.OptionParser('usage -t(get token)', version='%prog 1.0')
parser.add_option('-t', '--get-token', action='store_true', dest='gettoken', default=False, help='get 4s token')
parser.add_option('-r', '--read-file', dest='txt', type='string', help='read a list of client id and client secret')

opts, args = parser.parse_args()

# todo
def read_file(filename):
    print filename
    cli_ids = []
    cli_sec = []
    return

#todo
def login(username, password):


def get_token(cli_id, cli_sec, redirect_uri):
    client_id = cli_id
    client_secret = cli_sec
    client = foursquare.Foursquare(client_id=client_id, client_secret=client_secret, redirect_uri='http://127.0.0.1:3000/auth/return')
    
    home_url = 'https://foursquare.com/login'
    auth_url = client.oauth.auth_url()
    
    session = requests.session()

    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Host": "foursquare.com",
            "Upgrade-Insecure-Requests": "1",
         }

    html = session.get(home_url).content
    homepage = BS(html, 'html.parser')
    _xsrf = homepage.find('input', {'name': 'fs-request-signature'})['value']
    
    data = {
            'emailOrPhone':'username',
            'password':'password',
            'fs-request-signature': _xsrf,
            }

    #login
    resp = session.post(home_url, data, headers)

    print 'get access token...'

    try:
        # for those first time get access token ,and for those already have the token will throw an exception
        html = session.get(auth_url).content
        authpage = BS(html, 'html.parser')
        _xsrf = authpage.find('input', {'name': 'fs-request-signature'})['value']
        data = {
                'shouldAuthorize': 'true',
                'fs-request-signature': _xsrf
                }
        # the stmt will throw a exception when send data
        resp1 = session.post(auth_url, data, headers)
    except requests.exceptions.ConnectionError, e:
        print 'access_token:'
        code = str(e).split('?')[1][5:53]
        access_token = client.oauth.get_token(code)
        print access_token

    return 
    
def main():
    if opts.gettoken:
        client_id = raw_input('Client ID: ')
        client_secret = raw_input('Client Secret: ')
        redirect_uri = raw_input('Redirect uri: ')
        get_token(client_id, client_secret, redirect_uri)


if __name__ =='__main__':
    main()
