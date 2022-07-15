## Internal /editorial contribution process
The RDM-guidelines repository has an editorial group consisting of member of SciLifeLab's Data Centre and NBIS data management teams.

There is a list of [current resources](https://github.com/ScilifelabDataCentre/RDM-guidelines/blob/main/current-resources-list.md), with the web pages identified to either be of interest to link to, or to be incorporated into the guidelines. Also, keep in mind that the goal is not to duplicate what is in the [RDMkit](https://rdmkit.elixir-europe.org/) but rather add the Swedish flavour, and link to RDMkit for more information.

The steps below outlines the mutually agreed steps in order to update the RDM-guidelines repository:

1. Create a [New issue](https://github.com/ScilifelabDataCentre/RDM-guidelines/issues) describing the needed update. If appropriate, add a label with the level of priority, e.g. `MVP` if the update is needed previous to first release of the guidelines.
1. The person(s) that decides to resolve the issue sets themselves as assignee, so that the others in the editorial group know that the update is ongoing.
1. The assignee creates a branch: under **Development** in the menu on the right, click on the link `Create a branch`.
1. If the issue is a missing page:
    1. Create the new page either in folder [content/topic](https://github.com/ScilifelabDataCentre/RDM-guidelines/tree/main/content/topic) (most likely) or [content/data-life-cycle](https://github.com/ScilifelabDataCentre/RDM-guidelines/tree/main/content/data-life-cycle).
    1. Add metadata header to the top of the page by copying the header in [TEMPLATE_topic.md](https://github.com/ScilifelabDataCentre/RDM-guidelines/tree/main/TEMPLATE_topic.md).
    1. Remember to add link to the new page in the main index page ([content/_index.md](https://github.com/ScilifelabDataCentre/RDM-guidelines/blob/main/content/_index.md)) as well as the topic index page ([content/topic/_index.md](https://github.com/ScilifelabDataCentre/RDM-guidelines/blob/main/content/topic/_index.md)) (or if this is a new data-life-cycle page [content/data-life-cycle/_index.md](https://github.com/ScilifelabDataCentre/RDM-guidelines/blob/main/content/data-life-cycle/_index.md)).
    1. If appropriate, add links from other pages to this new page.
    1. If there is a resource or training link, add a heading last called 'Resources & Training' and put the link(s) in bullet list.
1. When it is time for a **Pull request**, add a link to the issue in the describing text (type a `#` and suggestions of possible links will appear). It is up to everyone in the editorial group to check if there are pull requests waiting to be approved.
