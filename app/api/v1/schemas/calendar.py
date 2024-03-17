
from typing import List, Optional
from pydantic import BaseModel

class IssueType(BaseModel):
    self: str
    id: int
    description: str
    iconUrl: str
    name: str
    subtask: bool
    fields: Optional[dict]
    statuses: List[str]
    namedValue: str

class Priority(BaseModel):
    self: str
    id: int
    name: str
    iconUrl: str
    namedValue: str

class StatusCategory(BaseModel):
    self: str
    id: int
    key: str
    colorName: str
    name: str

class Status(BaseModel):
    self: str
    description: str
    iconUrl: str
    name: str
    untranslatedName: Optional[str]
    id: int
    statusCategory: StatusCategory
    untranslatedNameValue: Optional[str]

class Component(BaseModel):
    pass  # Define fields if needed

class Watchers(BaseModel):
    self: str
    watchCount: int
    isWatching: bool

class Sla(BaseModel):
    id: str
    name: str
    _links: dict
    completedCycles: List[dict]
    ongoingCycle: dict

class RequestType(BaseModel):
    id: str
    _links: dict
    name: str
    description: str
    helpText: str
    issueTypeId: str
    serviceDeskId: str
    groupIds: List[str]
    icon: dict

class CurrentStatus(BaseModel):
    status: str
    statusCategory: str
    statusDate: dict

class CommentAuthor(BaseModel):
    self: str
    name: Optional[str]
    key: Optional[str]
    accountId: str
    emailAddress: Optional[str]
    avatarUrls: dict
    displayName: str
    active: bool
    timeZone: Optional[str]
    groups: Optional[List[str]]
    locale: Optional[str]
    accountType: str

class Comment(BaseModel):
    self: str
    id: int
    author: CommentAuthor
    body: str
    renderedBody: Optional[str]
    updateAuthor: CommentAuthor
    created: int
    updated: int
    visibility: Optional[dict]

class User(BaseModel):
    self: Optional[str]
    name: str
    key: str
    accountId: str
    emailAddress: Optional[str]
    avatarUrls: dict
    displayName: str
    active: bool
    timeZone: Optional[str]
    groups: Optional[List[str]]
    locale: Optional[str]
    accountType: str

class Issue(BaseModel):
    self: str
    id: int
    key: str
    changelog: dict
    fields: dict
    renderedFields: Optional[dict]

class IssueComment(BaseModel):
    self: str
    id: int
    author: CommentAuthor
    body: str
    renderedBody: Optional[str]
    updateAuthor: CommentAuthor
    created: int
    updated: int
    visibility: Optional[dict]

class IssueUser(BaseModel):
    self: Optional[str]
    name: str
    key: str
    accountId: str
    emailAddress: Optional[str]
    avatarUrls: dict
    displayName: str
    active: bool
    timeZone: Optional[str]
    groups: Optional[List[str]]
    locale: str
    accountType: str

class JiraDataRequest(BaseModel):
    issue: Issue
    comment: IssueComment
    user: IssueUser
    timestamp: int
    
    
    
class CalendarResponse(BaseModel):
    link: str