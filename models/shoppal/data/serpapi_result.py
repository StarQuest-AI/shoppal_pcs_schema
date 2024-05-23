
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Dict, Union
from uuid import UUID

from pydantic import BaseModel, Field


class searchParameters(BaseModel):
    q: str
    gl: str
    hl: str
    autocorrect: bool
    page: int
    type: str


class attributes(BaseModel):
    Headquarters: str
    CEO: str
    Founded: str
    Sales: str
    Products: str
    Founders: str
    Subsidiaries: str


class knowledgeGraph(BaseModel):
    title: str
    type: str
    website: str
    imageUrl: str
    description: str
    descriptionSource: str
    descriptionLink: str
    attributes: attributes


class sitelinks(BaseModel):
    title: str
    link: str


class organic(BaseModel):
    title: str
    link: str
    snippet: str
    sitelinks: Optional[List[sitelinks]]
    position: int
    date: Optional[str]


class peopleAlsoAsk(BaseModel):
    question: str
    snippet: str
    title: str
    link: str


class relatedSearches(BaseModel):
    query: str


class SerpApiResult(BaseModel):
    searchParameters: searchParameters
    knowledgeGraph: knowledgeGraph
    organic: List[organic]
    peopleAlsoAsk: List[peopleAlsoAsk]
    relatedSearches: List[relatedSearches]
