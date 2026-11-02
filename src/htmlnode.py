
class HtmlNode:
    def __init__(self, tag = None , value = None, children: list | None = None, props: dict[str, str] | None = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self) -> str:
        return f"Tag: {self.tag} | Value: {self.value} | Children: {self.children} | Props: {self.props}"

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self) -> str:
        fstr = ""
        if isinstance(self.props, dict):
            for k,v in self.props.items():
                fstr += f' {k}="{v}"'
        return fstr
