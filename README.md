**Objective**

Create a CRUD application that encapsulates the core modules presented throughout training using supporting tools, methodologies, and technologies.

To simplify, I have to create an application that uses the CRUD(Create, Read, Update and Delete) functions, by using the software’s, resources and techniques that have been provided to me throughout my training program.

**What I plan to create**

I plan to create an app that allows users to view MMA fighters that are signed to a particular MMA promotion. Users will be able to input details of a fighter and assigning it to the details of a promotion. To better explain the CRUD functionality of the app, check the table below.

|**CRUD**|
| :-: |
|Create |<p>- Promotion</p><p>- Fighter</p>|
|Read|<p>- Promotion</p><p>- Fighter</p>|
|Update|- Fighter|
|Delete|- Fighter|

The update and delete only contains fighter. This is considering that a fighter may change their weight class, thus needing an update or leaving a promotion. It is also banking on the fact that the promotion always exists therefore not needing to be updated or deleted.



**User Stories, Acceptance Criteria & Story Points**

User stories were implemented to create a vision of what the end product would look like. A user story is a description of an end goal from the user's point of view. ​To understand what a feature requires, an acceptance criterion is attached to the user stories. 

Also attached to the user story are story points. Story points are a way of estimating how much work is required to finish a task. To determine the story point given to a user story PlanningPoker.com. Using the Fibonacci sequence each user story was assigned a number based on difficulty to determine the story point.

- As a product owner, I want to add and remove fighters, so that I can size up potential fights, with a story point value of 13.

Given the user is on the home page, when they enter the fighter’s details, they can add and delete entries.

- As a user (fan), I want to view promotions, so that I know what promotion my favourite fighter is signed for, with a story point value of 3.

Given the user is on the homepage, when they have selected a promotion, they can view the fighters.

- As a user (fighter), I want to view fighters, so that I can see which fighters are in my weight division, with a story point value of 3.

Given the user is on the homepage, when they have selected a promotion, they can view fighters in their weight class.

**ERD**

The ERD (Entity-Relationship Diagram), represents a one-to-many relationship between promotions and fighters table. The one-to-many link dictated that one promotion can have many fighters, but a fighter cannot have many promotions.

The chosen ERD style was UML as it looks for presentable and easy to understand in comparison to Chen. The UML style keep entity types and attributes together whereas in Chen the entity types and attributes are branched out into their own cells.

![A screenshot of a computer

Description automatically generated](Aspose.Words.393f4e9a-c96a-4c30-8381-6662c1ea0c8e.001.png)

**CI Pipeline**

**Project Management – Trello & MVP**

In order to track the progress of the project, Trello was used. The way the board had been laid out was fairly simple. Three columns, ‘to do’, ‘doing’ and ‘done’. The list of tasks would be placed in ‘to do’. When a task was in progress it would be moved into ‘doing’ and upon completion over to ‘Done’.

Each task has been assigned a coloured tab. The coloured tab represents MoSCoW. MoSCoW is a prioritisation technique used for managing requirements. 


|MoSCoW|
| :-: |
|Must Have|The project would not be viable if these prerequisites were not met. These are components of the requirements in order to guarantee a minimum viable product (MVP) is achieved.|
|Should Have|Tasks that would have a noteworthy positive effect on the project.|
|Could Have|Tasks that could be done if there is enough time.|
|Won’t Have|Tasks that will be left out.|


The Trello board only contains two colours, these represent:

- Red – Must Have (MVP – Minimum Viable Product)
- Orange – Should Have

![A screenshot of a computer

Description automatically generated](Aspose.Words.393f4e9a-c96a-4c30-8381-6662c1ea0c8e.002.png)

This is due to the tasks included only contains tasks that were a necessary part of the project and those that would improve the project in a major way.

**Risk Assessment**

![](Aspose.Words.393f4e9a-c96a-4c30-8381-6662c1ea0c8e.003.png)The risk assessment was one of the first tasks to get underway. It was a way to see what tasks needed to be done as well as planning out other tasks. Making note of potential risks informs an individual ensuring they are aware of what may occur prior to undergoing a particular task.


**App – What it looks like?**

**Testing**

**Issues**

**Improvements**

Story points – 

Creating story points, in particular using planningpoker.com to create story points wasn’t the best idea for this project. This is due to the project being an individual project. The best/common practice for using story points is with a group project as the chosen story points cause a discussion and different perspectives may bring everyone to a common point.

Project Management – 

When using the MoSCoW technique it would be useful if I included Could Have and Won’t Have tasks. Not only would it dictate what the application may have looked like or the ideas for a better application, however it could be a start point for a future project or an update on the current application.

Other improvements – 


**Authors**

Mahammed Kassam

**Acknowledgements**

Many thanks go to the trainer, Earl Gray, for all his help, guidance, and patience. The cohort of 22MarEnable1 deserve to be acknowledged for their support and friendly demeanour. Not forgetting Leon Robinson for taking lead on a few sessions at short notice and also Harry Volker for being available to answer questions .

Thanks go to getbootstrap for their navbar.