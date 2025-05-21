import xml.dom.minidom # for DOM parsing
import xml.sax # for SAX parsing
from datetime import datetime # for timing

# DOM parsing

def dom_parse():
    start = datetime.now()
    doc = xml.dom.minidom.parse("go_obo.xml") # parse the XML file
    terms = doc.getElementsByTagName('term') # get all the terms
    max_counts = {                        
        'molecular_function': {'count': 0, 'id': None},
        'biological_process': {'count': 0, 'id': None},
        'cellular_component': {'count': 0, 'id': None}
    }  # Set up a dictionary to keep track of the maximum counts for each namespace
    for term in terms:
        namespace_elements = term.getElementsByTagName('namespace') # get the namespace element
        if not namespace_elements: 
            continue  # skip terms without a namespace
        namespace_node = namespace_elements[0].firstChild # get the text content of the namespace element
        is_a_list = term.getElementsByTagName('is_a')  # get the is_a elements
        count = len(is_a_list)  # count the number of is_a elements
        if count > max_counts[namespace_node.data]['count']:
            max_counts[namespace_node.data]['count'] = count  # update the maximum count if necessary
            id_elements = term.getElementsByTagName('id')  # get the id element
            id_node = id_elements[0].firstChild  # get the text content of the id element
            max_counts[namespace_node.data]['id'] = id_node.data # update the id if necessary
    end = datetime.now() # get the end time
    print("\nDOM Results:")
    for namespace, data in max_counts.items(): 
        print(f"{namespace}: Term {data['id']} with {data['count']} is_a elements") 
    return end - start

# SAX parsing

class GoboSaxHandler(xml.sax.ContentHandler): # define a class to handle the SAX events
    def __init__(self):
        super().__init__()
        self.current_data = ""
        self.in_term = False # flag to indicate if we are inside a term element
        self.current_id = ""
        self.current_namespace = ""
        self.is_a_count = 0 # count of is_a elements for the current term
        self.max_counts = {
            'molecular_function': {'count': 0, 'id': ''},
            'biological_process': {'count': 0, 'id': ''},
            'cellular_component': {'count': 0, 'id': ''} 
        } # Set up a dictionary to keep track of the maximum counts for each namespace

    def startElement(self, name, attrs): # handle the start of an element
        if name == 'term':
            self.in_term = True
            self.current_id = ""
            self.current_namespace = ""
            self.is_a_count = 0
        elif self.in_term:
            if name == 'id':
                self.current_data = ""
            elif name == 'namespace':
                self.current_data = ""
            elif name == 'is_a':
                self.is_a_count += 1 # increment the is_a count for the current term
    
    def characters(self, content): # handle character data
        if self.in_term:
            self.current_data += content.strip() # strip whitespace from the data

    def endElement(self, name): # handle the end of an element
        if name == 'term':
            self.in_term = False # we are no longer inside a term element
            if self.current_namespace in self.max_counts:
                current_entry = self.max_counts[self.current_namespace] # get the current entry for the current namespace
                if self.is_a_count > current_entry['count']: # update the maximum count if necessary
                    current_entry['count'] = self.is_a_count # update the count
                    current_entry['id'] = self.current_id # update the id
        elif name == 'id':
            self.current_id = self.current_data # update the current id
            self.current_data = ""
        elif name == 'namespace':
            self.current_namespace = self.current_data # update the current namespace
            self.current_data = ""

def sax_parse(): # parse the XML file using SAX
    start = datetime.now()
    parser = xml.sax.make_parser()
    handler = GoboSaxHandler()
    parser.setContentHandler(handler) # set the content handler
    parser.parse("go_obo.xml") # parse the XML file
    end = datetime.now() 
    print("\nSAX Results:")
    for namespace, data in handler.max_counts.items():
        print(f"{namespace}: Term {data['id']} with {data['count']} is_a elements")
    return end - start # return the time taken to parse the file

if __name__ == "__main__":
    print("Processing with DOM...")
    dom_duration = dom_parse()
    print("\nProcessing with SAX...")
    sax_duration = sax_parse()
    print(f"\nDOM Time: {dom_duration}")
    print(f"SAX Time: {sax_duration}")
    if dom_duration < sax_duration: # compare the times taken to parse the file
        print("# DOM was faster")
    else:
        print("# SAX was faster")