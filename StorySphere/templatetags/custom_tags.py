from django import template
from StorySphere.models import ForumComment  # Import your ForumComment model

register = template.Library()

@register.simple_tag
def get_comments_for_topic(topic_id):
    return ForumComment.objects.filter(topic_id=topic_id)
