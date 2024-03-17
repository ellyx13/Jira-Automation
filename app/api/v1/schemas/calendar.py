
from typing import List, Optional
from pydantic import BaseModel

class User(BaseModel):
    self: Optional[str] = None
    name: str
    key: str
    accountId: str
    emailAddress: Optional[str] = None
    avatarUrls: dict
    displayName: str
    active: bool
    timeZone: Optional[str] = None
    groups: Optional[dict] = None
    locale: Optional[str] = None
    accountType: str

class IssueType(BaseModel):
    self: str
    id: int
    description: str
    iconUrl: Optional[str] = None
    name: str
    untranslatedName: Optional[str] = None 
    subtask: bool
    fields: Optional[dict] = None
    statuses: List[str] = None
    namedValue: str

class Priority(BaseModel):
    self: str
    id: int
    name: str
    iconUrl: Optional[str] = None
    namedValue: str

class Assignee(BaseModel):
    self: str
    name: Optional[str] = None
    key: Optional[str] = None
    accountId: str
    emailAddress: Optional[str] = None 
    avatarUrls: dict
    displayName: str
    active: bool
    timeZone: str
    groups: Optional[dict] = None
    locale: Optional[str] = None
    accountType: str

class Project(BaseModel):
    self: str
    id: int
    key: str
    name: str
    description: Optional[str] = None
    avatarUrls: dict
    issuetypes: Optional[dict] = None
    projectCategory: Optional[dict] = None
    email: Optional[str] = None
    lead: Optional[dict] = None
    components: Optional[dict] = None
    versions: Optional[dict] = None
    projectTypeKey: str
    simplified: bool

class Status(BaseModel):
    self: str
    description: str
    iconUrl: str
    name: str
    untranslatedName: Optional[str] = None
    id: int
    statusCategory: dict
    untranslatedNameValue: Optional[str] = None

class Watches(BaseModel):
    self: str
    watchCount: int
    isWatching: bool

class Fields(BaseModel):
    statuscategorychangedate: str
    issuetype: Optional[IssueType] = None
    project: Optional[Project] = None
    fixVersions: List[dict] = None
    workratio: int
    issuerestriction: dict
    watches: Optional[Watches] = None
    created: int
    priority: Optional[Priority] = None
    labels: List[str] = None
    versions: List[dict] = None
    issuelinks: List[dict] = None
    assignee: Optional[Assignee] = None
    updated: int
    status: Optional[Status] = None
    components: List[dict] = None
    description: Optional[str] = None
    timetracking: dict
    attachment: List[dict] = None
    summary: str
    creator: Optional[Assignee] = None
    subtasks: List[dict] = None
    reporter: Optional[Assignee] = None
    aggregateprogress: dict
    progress: Optional[dict] = None
    votes: Optional[dict] = None
    comment: Optional[dict] = None
    worklog: Optional[dict] = None

class Changelog(BaseModel):
    startAt: int
    maxResults: int
    total: int

class Issue(BaseModel):
    self: str
    id: int
    key: str
    changelog: Optional[Changelog] = None
    fields: Optional[Fields] = None

class JiraDataRequest(BaseModel):
    issue: Issue
    user: User
    timestamp: int

    
    
    
class CalendarResponse(BaseModel):
    link: str