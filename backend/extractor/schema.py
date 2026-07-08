from pydantic import BaseModel
from typing import List

class Feature(BaseModel):
    name: str

class ProofPoint(BaseModel):
    metric: str
    value: float
    unit: str

class Product(BaseModel):
    name: str

class Persona(BaseModel):
    title: str

class ICPSegment(BaseModel):
    industry: str

class ExtractionResult(BaseModel):
    product: Product
    features: List[Feature]
    proof_points: List[ProofPoint]
    persona: Persona
    icp_segment: ICPSegment