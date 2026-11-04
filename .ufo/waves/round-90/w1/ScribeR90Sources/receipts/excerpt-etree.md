# excerpt — https://docs.python.org/3/library/xml.etree.elementtree.html (raw sha256 001033d3367e8dd0fbf3c85174aa96cdf305a90f3f1219970b4138075fb047f6; text = tags stripped, whitespace collapsed)

## E-parse (offset 3579 in normalized text, 17 words)

```
child.tag, child.attrib) ... country {'name': 'Liechtenstein'} country {'name': 'Singapore'} country {'name': 'Panama'} Children are nested, and we can access specific child nodes by index: >>> root[0][1].text '2008' Note Not all elements of the XML input will end up as elements of the parsed tree. Currently, this module skips over any XML comments, processing instructions, and document type declarations in the input. Nevertheless, trees built using this module’s API rather than parsing from XML text can have comments and processing instructions in them; they will be included when generating XML output. A document type declaration may be accessed by passing a custom TreeBuilder instance to the XMLParser construc
```

## E-comment (offset 17926 in normalized text, 16 words)

```
n version 3.8. xml.etree.ElementTree.Comment(text=None)¶ Comment element factory. This factory function creates a special element that will be serialized as an XML comment by the standard serializer. text is a string containing the comment string. Returns an element instance representing a comment. Note that XMLParser skips over comments in the input instead of creating comment objects for them. An ElementTree will only contain comment nodes if they have been inserted into to the tree using one of the Element methods. xml.etree.ElementTree.dump(elem)¶ Writes an element tree or element structure to sys.stdout. This function should be used for debugging only. The exact output format is imple
```

## E-tb (offset 41839 in normalized text, 20 words)

```
a dict of attributes. It is expected to return a new element instance. The comment_factory and pi_factory functions, when given, should behave like the Comment() and ProcessingInstruction() functions to create comments and processing instructions. When not given, the default factories will be used. When insert_comments and/or insert_pis is true, comments/pis will be inserted into the tree if they appear within the root element (but not outside of it). close()¶ Flushes the builder buffers, and returns the toplevel document element. Returns an Element instance. data(data)¶ Adds text to the current element. data is a string. end(tag)¶ Closes the current element. tag is the element name. Returns the closed element. start(tag
```
