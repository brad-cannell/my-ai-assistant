# Categories and Tags

When creating a new course, course authors need to supply some metadata elements that help organize course content and make it easier for learners to find the information they need.

# Categories

**Categories** are used on the courses page to help learners filter and discover courses based on their interests.

## Categories in Use
To view the current categories in use, navigate to the courses page ( [https://dev.epi-workbench.com/EPIWorkBench/courses/](https://dev.epi-workbench.com/EPIWorkBench/courses/) ) and expand the course filter.

# Tags

**Tags** are used to facilitate the search and discovery of course content on the EWB platform. While **categories** help organize courses (e.g., _data analysis_), **tags** provide more granular detail, such as specific functions (_lm_ or _glm_). The primary purpose of tags is to help learners find the content they are looking for.

Tags can be assigned to both **courses and lessons**. Additionally, lessons **automatically inherit** the tags assigned to their parent course, ensuring consistency in searchability and organization.

> [!CAUTION] **Tag Inheritance**
> We are working on [tagging lessons instead of courses](https://trello.com/c/mCQyAXYf/116-tags-tag-lessons-instead-of-courses).

> [!WARNING] **YAML Headers**
> For now, when you add a tag to a lesson yaml header, also add it to the course README.

## Tag Courses

On the Course Edit page: 
- Click inside the Tag selection box
- Start typing to view available tags

> [!CAUTION] **Tag Selection**
> We are working on the ability to [type to search for tags](https://trello.com/c/5LnNpNdV/115-tags-type-to-search-for-tags?search_id=b44552a9-c9e9-4b2a-8507-351ff78ce6b0).
> [Add a screenshot when we are able](https://trello.com/c/JRvkjSdH/117-add-images-to-course-author-wiki-pages).

## Tags in Use

To view the current tags in use, navigate to the tags page. Here you can view all tags and their associated descriptions.

> [!WARNING] **Add Screenshot**
> [Add a screenshot when we are able](https://trello.com/c/JRvkjSdH/117-add-images-to-course-author-wiki-pages).

## Requesting new tags

Course authors can request a new tag in one of two ways:

1. From the Course Edit page. Click `Can't find a tag? Request a new one →` below the Tag selection box.

2. From the Course Author Dashboard. Click the `Tag Requests` link in the sidebar menu. 

> [!WARNING] **Add Screenshot**
> [Add a screenshots when we are able](https://trello.com/c/JRvkjSdH/117-add-images-to-course-author-wiki-pages).

### Tag guidelines

When requesting new tags, please keep the following guidelines in mind:
- Write the tag name in title case (e.g., "Categorical Data").
- When the tag applies to a function, use the language name (e.g., "Mean Function [R]".
- When the tag applies to a general concept, don't use the language name (e.g., "Missing Data").
- Always add a tag description.
- Don't use a tag if it will only be applied to one course or lesson?

When writing **tag descriptions**:
- Lead the tag description with "This course or lesson contains information about...". For example, "This course or lesson contains information about the structure and function of data frames, or explicitly discusses creating data frames."
- It can also be helpful to add "This tag is not intended for use when the course or lesson just happens to contain...". For example, "This tag is not intended for use when the course or lesson just happens to contain data frames."
