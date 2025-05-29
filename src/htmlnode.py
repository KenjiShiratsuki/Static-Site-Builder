class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        string = ""
        for prop in self.props:
            string += f' {prop}="{self.props[prop]}"'
        return string
    
    def __repr__(self):
        return f"{self.tag}, {self.value}, {self.children}, {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None or self.value == "":
            raise ValueError("invalid HTML: no value")
        elif self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    def to_html(self):
        if self.tag is None or self.tag == "":
            raise ValueError("Invalid HTML: no tag")
        elif self.children is None or self.children == []:
            raise ValueError("Invalid Parent Node: no children")
        return f"<{self.tag}{self.props_to_html()}>{"".join(map(lambda child: child.to_html(), self.children))}</{self.tag}>"