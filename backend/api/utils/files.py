class FileUtils():
    def properties(self, context):

        path = 'configuration/properties/'
        props_result = []

        if context == 'server':
            path += 'server.properties'

        elif context == 'boto':
            path += 'boto.properties'

        elif context == 'mlpsi2':
            path += 'mlpsi2.properties'

        elif context == 'new_schema':
            path += 'contabil.properties'

        elif context == 'dinah':
            path += 'dinah.properties'

        try:
            properties_file = open(path)

            for property in properties_file:
                property = property.strip()

                if (not property.startswith('#') and
                    property != ''):
                    props_result.append(property.split('='))
        finally:
            properties_file.close()

        return dict(props_result)
