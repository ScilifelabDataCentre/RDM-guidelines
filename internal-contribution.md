## Internal /editorial contribution process
The RDM-guidelines repository has an editorial group consisting of members of SciLifeLab's Data Centre and NBIS data management teams.

When adding content, keep in mind that the goal is not to duplicate what is in the [RDMkit](https://rdmkit.elixir-europe.org/) but rather add the Swedish flavour, and link to RDMkit for more information.

The steps below outlines the mutually agreed steps in order to update the RDM-guidelines repository:

1. Create a [New issue](https://github.com/ScilifelabDataCentre/RDM-guidelines/issues) describing the needed update. If appropriate, add a label with the level of priority.
1. The person(s) that decides to resolve the issue sets themselves as assignee, so that the others in the editorial group know that the update is ongoing.
1. The assignee creates a branch: under **Development** in the menu on the right, click on the link `Create a branch`.
1. If the issue is a missing page:
    1. Create the new page either in folder [content/topics](./content/topics) (most likely) or [content/data-life-cycle](./content/data-life-cycle).
    1. Add metadata header to the top of the page by copying the header in [TEMPLATE_topic.md](./TEMPLATE_topic.md).
    1. Remember to add link to the new page in the main index page ([content/_index.md](./content/_index.md)) as well as the topic index page ([content/topics/_index.md](./content/topics/_index.md)) (or if this is a new data-life-cycle page [content/data-life-cycle/_index.md](./content/data-life-cycle/_index.md)).
    1. If this is a new topic page, also [shortcode for display topics](./layouts/shortcodes/display-topics.html) needs to be updated with the new topic. <!-- not sure if more info is needed? -->
    1. If appropriate, add links from other pages to this new page.
    1. If there is a resource, remove the commented out characters in the Resources section, change '--add topic/title--' to the topic title, and add the resource to the [resources.json](./data/resources.json) page as outlined [below](#about-resources).
1. When it is time for a **Pull request**, if the branch wasn't created as described above, add a link to the issue in the describing text (type a `#` and suggestions of possible links will appear). It is up to everyone in the editorial group to check if there are pull requests waiting to be approved. All PRs should be reviewed by another member, if the update isn't minor (i.e. unlikely that typo:s or wrong links have been included).
2. When **merging** a Pull request, delete the branch being merged. Note that the linked issue will be automatically closed if using closing words. 

### About resources
A resource is any **external** links with information that is of added value for a page (topic or data life cycle page). Note that links to internal pages should only appear in the text.

There are currently three types of resources:

* Tool - any type of tool to assist in a data management task
* Training - courses or course catalogue links
* Guidance - any form of digital information material that is not explicitly training material (i.e. self paced training material is of type Training, not Guidance)

In order to add a resource:

1. Copy the item text (everything within the curly brackets, including the brackets themselves) in [TEMPLATE_resource.json](TEMPLATE_resource.json), and put it at the end of the [resources.json](./data/resources.json) file. 
1. Remember to add a comma after the last closing curly bracket of the previous item.
1. Remove all rows for which information does not exist, and update the values of the other rows as appropriate. Note that the last row of an item (before the closing curly bracket) should not end with a comma.

Note: If the resource itself already exist, and a page should have this resource appearing on its page, update the item in the [resources.json](./data/resources.json) file by adding the title of the page in the topic or phase row (e.g. `topic: ["Metadata","README files],` or `phase: ["Collect", "Share"],`).