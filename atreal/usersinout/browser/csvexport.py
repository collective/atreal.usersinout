""" Define a browser view csv export of a contact directory
"""

import csv
from StringIO import StringIO
from Products.Five.browser import BrowserView

field_list = [
    'portal_type',
    'title',
    'description',
    'firstname',
    'lastname',
    'job_title',
    'organization',
    'department',
    'address',
    'address_complement',
    'postcode',
    'city',
    'country',
    'email',
    'website',
    'office_phone',
    'mobile_phone',
    'private_phone',
    'fax_number',
]

class CsvExportView (BrowserView):
    """ Csv export view of a contact directory
    """
    
    def writeLine(self, writor, obj):
        fields = []
        for name in field_list:
            value = getattr(obj, name, '')
            if value is None:
                value = ""
            elif not isinstance(value, (str, unicode)):
                value = value.Title()
            fields.append(value)
        #data += ",".join(fields)+"\n"
        writor.writerow(fields)
    
    def __call__(self):
        pcon = self.context.portal_contacts
        dpath = '/'.join(self.context.getPhysicalPath())
        #data = ",".join(field_list)+"\n"
        datafile = StringIO()
        writor = csv.writer(datafile)
        writor.writerow(field_list)
        
        for brain in pcon(path={'query': dpath, 'depth': 1,},
                          portal_type="Organization"):
            obj = brain.getObject()
            self.writeLine(writor, obj)

        for brain in pcon(path={'query': dpath, 'depth': 1,},
                          portal_type="Contact"):
            obj = brain.getObject()
            self.writeLine(writor, obj)

        #return data
        self.request.response.addHeader('Content-Disposition', "attachment; filename=directory_export.csv")
        self.request.response.addHeader('Content-Type', "text/csv")
        self.request.response.addHeader('Content-Length', "%d" % datafile.len)
        self.request.response.addHeader('Pragma', "no-cache")
        self.request.response.addHeader('Cache-Control', "must-revalidate, post-check=0, pre-check=0, public")
        self.request.response.addHeader('Expires', "0")
        return datafile.getvalue()
    
