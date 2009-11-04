import csv
from Products.Five.browser import BrowserView
from atreal.usersinout import UsersInOutFactory as _
from atreal.usersinout.config import CSV_HEADER

class UsersInOut (BrowserView):
    """ Users import and export as CSV files
    
    """
    
    def __call__(self):
        method = self.request.get('REQUEST_METHOD', 'GET')
        if (method != 'POST') or not int(self.request.form.get('form.submitted', 0)):
            return self.index()
        
        if self.request.form.get('form.button.Cancel'):
            return self.request.response.redirect(self.context.absolute_url())
            
        if self.request.form.get('form.button.Import'):
            return self.importUsers()
            
        if self.request.form.get('form.button.Import'):
            return self.exportUsers()            
    
    
    def importUsers(self):
        """ Import users from CSV file.
            In case of error, return a CSV file filled with the lines where
            errors occured.
            
        """
        file_upload = self.request.form.get('csv_upload', None)
        if file_upload is None:
            return # XXX
        
        reader = csv.reader(file_upload)
        header = reader.next()[1:]
        
        for line in reader:
            
            for name, value in zip(header, line):
                print "Setting %s = %s" % (name, value)
                field = entry.getField(name)
                if field is None:
                    continue

    
        self.context.reindexObject()    
    

        message = _(u'The CSV file has been imported.',
                    mapping={u'title' : self.context.Title()})
        self.context.plone_utils.addPortalMessage(message)
        
        self.request.response.redirect(self.context.absolute_url())


    def exportUsers(self):
        """ Export users within CSV file.
            
        """    
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


    def _writeLine(self, writor, obj):
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
    