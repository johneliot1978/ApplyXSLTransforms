# Description: command line python script to apply xsl to an xml file and output the resulting transformed xml
import argparse
from lxml import etree

def apply_xslt(xml_file, xslt_file, output_file):
    # Load XML and XSLT files
    dom = etree.parse(xml_file)
    xslt = etree.parse(xslt_file)

    # Create XSLT transformation
    transform = etree.XSLT(xslt)

    # Apply transformation
    result = transform(dom)

    # Write output to file
    with open(output_file, 'wb') as f:
        f.write(etree.tostring(result, pretty_print=True))

def extract_unique_values(xml_file, tag):
    # Load XML file
    dom = etree.parse(xml_file)

    # Find all elements with the specified tag
    elements = dom.xpath(f'//{tag}')

    # Extract unique values from the elements
    unique_values = set()
    for element in elements:
        unique_values.add(element.text)

    return unique_values

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Apply XSLT transformation and extract unique values from specified XML tag.')
    parser.add_argument('xml_file', type=str, help='Input XML file path')
    parser.add_argument('xslt_file', type=str, help='XSLT file path')
    parser.add_argument('output_file', type=str, help='Output XML file path')
    parser.add_argument('--tag', type=str, help='XML tag to extract unique values from')

    args = parser.parse_args()

    # Apply XSLT transformation
    apply_xslt(args.xml_file, args.xslt_file, args.output_file)

    if args.tag:
        # Extract and print unique values from the specified tag
        unique_values = extract_unique_values(args.xml_file, args.tag)
        print("Unique values in <", args.tag, ">:")
        for value in unique_values:
            print(value)
