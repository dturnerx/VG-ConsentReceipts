""" This is a module to print a Kantara Consent Receipt based on version 1.1"""
import json
# import webbrowser

with open('KI_CR_1.1.0-Example.json', encoding='utf-8', newline='\r\n') as data_file:
    J_CRDATA = json.loads(data_file.read())
    print('version: {}'.format(J_CRDATA['version']))
    print(J_CRDATA['version'], '\n',
          J_CRDATA['jurisdiction'], '\n',
          J_CRDATA['consentTimestamp'],
          J_CRDATA['collectionMethod'],
          J_CRDATA['consentReceiptID'],
          J_CRDATA["publicKey"],
          J_CRDATA['language'],
          J_CRDATA['piiPrincipalId'],
          sep='')
    for piiController in J_CRDATA['piiControllers']:
        print(piiController['piiController'])
        for service in J_CRDATA['services']:
            print(service['service'])
            for purpose in service['purposes']:
                print('    Purpose: %s' % purpose['purpose'])
                print('        Purpose category: %s' %  purpose['purposeCategory'])
                print('        piiCategory: %s' %  purpose['piiCategory'])
                print('        primaryPurpose: %s' %  purpose['primaryPurpose'])
                print('        termination: %s' %  purpose['termination'])
                print('        thirdPartyDisclosure: %s' %  purpose['thirdPartyDisclosure'])
                if 'thirdPartyName' in purpose:
                    print('        thirdPartyName: %s' %  purpose['thirdPartyName'])

# webbrowser.open('cr.py', new=1)
