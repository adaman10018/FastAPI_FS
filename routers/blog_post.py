from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel
from typing import Optional, List


router = APIRouter(
    prefix = '/blog',
    tags = ['blog']
)

class BlogModel(BaseModel):
    title: str
    content: str
    num_comments: int
    published: Optional[bool]

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'data': blog,
        'id': id,
        'version': version        
    }

@router.post('/new/{id}/comment/{comment_id}')
def create_comment(
    blog: BlogModel, 
    id: int, 
    comment_title: int = Query(
        None, 
        title='Title of the comment', 
        description='Some description for comment_title',
        alias='commentTitle',
        deprecated=True
    ),
    content: str = Body(
        ...,  # ... (Ellipsis) makes content required
        min_length=10,
        max_length=12,
        regex='^[a-z\s]*$'
    ),
    v: Optional[List[str]] = Query(['1.0', '1.1', '1.2']),
    comment_id: int = Path(..., gt=5, le=10) 
):

    return {
        'blog': blog,
        'id': id,
        'comment_title': comment_title,
        'content': content,
        'version': v,
        'comment_id': comment_id,
    }