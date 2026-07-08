from dataclasses import dataclass

@dataclass
class Node:
    id: str
    label: str
    properties: dict


@dataclass
class Edge:
    source: str
    relation: str
    target: str


@dataclass
class KnowledgeGraph:
    nodes: list
    edges: list