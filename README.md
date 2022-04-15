# The MMA App

### Objective

Create a CRUD application that encapsulates the core modules presented throughout training using supporting tools, methodologies, and technologies.

To simplify, I have to create an application that uses the CRUD(Create, Read, Update and Delete) functions, by using the software&#39;s, resources and techniques that have been provided to me throughout my training program.

### What I plan to create

I plan to create an app that allows users to view MMA fighters that are signed to a particular MMA promotion. Users will be able to input details of a fighter and assigning it to the details of a promotion. To better explain the CRUD functionality of the app, check the table below.

| CRUD | Applied on |
| --- | --- |
| Create | - Promotions 
- Fighters |
| Read | - Promotions 
- Fighters |
| Update | - Fighters | 
| Delete | - Fighters 
- Promotions |

### User Stories, Acceptance Criteria &amp; Story Points

User stories were implemented to create a vision of what the end product would look like. A user story is a description of an end goal from the user&#39;s point of view. To understand what a feature requires, an acceptance criterion is attached to the user stories.

Also attached to the user story are story points. Story points are a way of estimating how much work is required to finish a task. To determine the story point given to a user story PlanningPoker.com. Using the Fibonacci sequence each user story was assigned a number based on difficulty to determine the story point.

- As a product owner, I want to add and remove fighters, so that I can size up potential fights, with a story point value of 13.
  Given the user is on the home page, when they enter the fighter&#39;s details, they can add and delete entries.

- As a user (fan), I want to view promotions, so that I know what promotion my favourite fighter is signed for, with a story point value of 3.
  Given the user is on the homepage, when they have selected a promotion, they can view the fighters.

- As a user (fighter), I want to view fighters, so that I can see which fighters are in my weight division, with a story point value of 3.
  Given the user is on the homepage, when they have selected a promotion, they can view fighters in their weight class.

### ERD

The ERD (Entity-Relationship Diagram), represents a one-to-many relationship between promotions and fighters table. The one-to-many link dictated that one promotion can have many fighters, but a fighter cannot have many promotions.

The chosen ERD style was UML as it looks for presentable and easy to understand in comparison to Chen. The UML style keep entity types and attributes together whereas in Chen the entity types and attributes are branched out into their own cells.

![1UML](https://user-images.githubusercontent.com/101266645/163552586-087dfd2f-7f61-4b75-b143-960a1179b145.png)

### CI Pipeline

![2CIPipeline](https://user-images.githubusercontent.com/101266645/163552551-71d24848-5114-432b-8f95-757105c9eb02.png)

| CI Pipeline | What was done in this project |
| --- | --- |
| Project Tracking – Trello | Work is set out and branches/tasks are created on Version Control System. |
| Version Control System – Git &amp; GitHub | Git – Software on computer that takes snapshots of work done. GitHub – Remote destination that snapshots can be pushed to. |
| Source Code - Developer | Pulls down latest version of code.Can push up to main branch. |
| CI Server – Jenkins | Loaded onto a VM in the cloud.GitHub repository link attached to Jenkins in order to build tool. |
| Built Tool | Run lines of code and build it into a working application. |
| Automated Testing | Once built into a working application, automated tests will be running to test functionality. Tests will be sent back to the build tool then back to Jenkins for developer to be notified to make changes or if tests have passed. |
| Live Environment | Similar to live environment except not connected to end user. Allows developers opportunity to play around with the product. |

### Project Management – Trello &amp; MVP

In order to track the progress of the project, Trello was used. The way the board had been laid out was fairly simple. Three columns, &#39;to do&#39;, &#39;doing&#39; and &#39;done&#39;. The list of tasks would be placed in &#39;to do&#39;. When a task was in progress it would be moved into &#39;doing&#39; and upon completion over to &#39;Done&#39;.

Each task has been assigned a coloured tab. The coloured tab represents MoSCoW. MoSCoW is a prioritisation technique used for managing requirements.

| MoSCoW | Explanation |
| --- | --- |
| Must Have | Anything required to make the project work. These are components of the requirements in order to guarantee a minimum viable product (MVP) is achieved. |
| Should Have | Tasks that would have a noteworthy positive effect on the project. |
| Could Have | Tasks that could be done if there is enough time. |
| Won&#39;t Have | Tasks that will be left out. |

The Trello board only contains two colours, these represent:

- Red – Must Have (MVP – Minimum Viable Product)
- Orange – Should Have

![3Trello](https://user-images.githubusercontent.com/101266645/163552827-b84270aa-e1cf-4976-bca4-2e42aa1cbede.png)

This is due to the tasks included only contains tasks that were a necessary part of the project and those that would improve the project in a major way.

### Risk Assessment

Risk Assessments are used to ensure a project&#39;s success by evaluating scenarios that may impact the project in a negative way. Making note of potential risks informs an individual ensuring they are aware of what may occur prior to undergoing a particular task. By evaluating risks, I am able to mitigate the damage that may be caused to the project and may design the project such that theses risks are less likely to occur.

| Description | Evaluation | Likelihood | Impact Level | Responsibility | Current Control Measures | Proposed Control Measures | Response |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Program Freezes | Work done may get lost | Med | High | Mahammed Kassam | None | Have multiple backups saved in different locations | Open up autosaved/backup or start project again |
| Cloud server goes down | Users may not be able to access some of their data | Low | High | Google Cloud Platform | None | Have backup saved on computer | If solely working on cloud server, only thing that can be done is to wait. If a backup is available, continue on the backup. |
| Data not being presented neatly | Code will be hard to read and may turn others from having a look at it | High | Med | Mahammed Kassam | Ensure data is readable to myself | Make sure someone else looks over data to ensure it&#39;s not just readable to myself | Neaten up data |
| Requirement/ dependencies not installed | Program will not understand code | High | Low | Mahammed Kassam | Install dependency when VS code doesn&#39;t recognise code typed | Have a file that contains all the requirements/ dependencies beforehand and install it at the start | Install the requirement/ dependency |
| VMs private ID being used instead of public ID | Everyone will have access to the private ID | High | High | Mahammed Kassam | Ensuring public ID is copied | Constantly check the public ID is being used | Delete VM and create a new one |
| Computer/laptop becoming slow | Programs will respond slowly or even eventually close | High | High | PC/Laptop | Only opening necessary files, programs, and browsers | Getting a PC/laptop with a better processor and a bigger RAM | Stay patient, and close unnecessary applications |
| Team Leader away | Slow down the project, take longer to complete | Low | Med | No-one | Have fellow team members to support when needed | Make connections so there are more options when it comes to support in time of need | Have fellow colleagues and other leaders review project progression |
| Not knowing where to start | Shorten the time left to complete the project | Med | High | Mahammed Kassam | Start with non-coding related tasks first i.e., User stories, Risk Assessment, Story Points, Entity Diagrams etc. to get a rough idea of what will be created | Same as current control measures - Start with non-coding related tasks first i.e., User stories, Risk Assessment, Story Points, Entity Diagrams etc. to get a rough idea of what will be created | Seek advice from fellow colleagues or team leaders as they would have been in the same situation |
| Internet going down | Won&#39;t be able to run instances, which in turn will result in not being able to access work saved to cloud | Med | High | Internet Provider | None | Some cloud providers offer offline access. Whether it being a part of a normal or premium account, ensure the cloud provider has this option | Switch to offline access, which gives access to files stored in the cloud without an internet connection |
| Deleting VM | All work will be lost | Low | High | Mahammed Kassam | Using GitHub to back work up | Along with using GitHub snapshots of the VM can be taken and used to restore previous memory | Git clone last push from GitHub |

### App – What it looks like?

The front-end design was kept very introductory, having a navigation bar that is understandable and can be easily used. Upon entering the URL, the user is welcomed to the home page.

![4Homepage](https://user-images.githubusercontent.com/101266645/163552998-714d1d67-30fd-4fa2-9cef-8ecefdf3078e.png)

Cycling through the navigation, a user may choose to add a promotion. Here they will be presented with three input fields, a promotion name, owner and based.

![5AddAPromotion](https://user-images.githubusercontent.com/101266645/163553096-107a582f-4118-43c1-814b-e1e30bb6f481.png)

Once a promotion has been added the user can thereafter view the promotion they have added. Here the user will see all previous entries and can decide upon which they want to be deleted.

![6ViewAllPromotions](https://user-images.githubusercontent.com/101266645/163553259-02a90aa9-f13c-4988-af56-db2c95cbbc3e.png)

Every promotion needs fighters. The user can enter fighter details on the next navigation tab. The requirement fields are, fighter name, fighters weight class which is a select field, country the fighter is based and promotion name which can only be of those promotions that have been added.

![7AddAFighter](https://user-images.githubusercontent.com/101266645/163553311-61649f32-1d61-462e-bd54-10a254d736a8.png)

Having entered the fighters&#39; details, the user can then view the fighters where they have the option to update the fighters details, which updates everything besides the promotion name, and also delete a fighter.

![8ViewFighters](https://user-images.githubusercontent.com/101266645/163553379-1ef8d757-a76c-4b66-bf8d-f4acf3ddcfe6.png)

### Testing and Issues

Below is the code created to run the tests

![9Test1](https://user-images.githubusercontent.com/101266645/163553502-c393d63d-c2f0-4c7b-a617-22b02d75a1c7.png)

![10test2](https://user-images.githubusercontent.com/101266645/163553516-cd2449d6-f1d7-41ee-b123-939296c029da.png)

When initially running the code almost all the tests failed. However, I ensured to make edits to get the pass rate above 80%. One the main issues encountered was the status code for a delete function. For a working route the status code needed to be 200, however this is different for a delete route which is 302. Another issue was adding the correct parameter/argument within the url\_for. This involved a lot of referring back to other files to ensure the parameter inserted was correct.

![](RackMultipart20220411-4-mw5liq_html_d4244587b2396808.png)As for the 1 failed test, time was spent trying to covert it to passed but I was unsuccessful. Given more time I probably would have succeeded. Included below are the results from VS Code and also Jenkins.

![](RackMultipart20220411-4-mw5liq_html_21e5efb506d71635.png)

![](RackMultipart20220411-4-mw5liq_html_7a39eb8c1c9f1e2.png)

### Improvements

Story points –

Creating story points, in particular using planningpoker.com to create story points wasn&#39;t the best idea for this project. This is due to the project being an individual project. The best/common practice for using story points is with a group project as the chosen story points cause a discussion and different perspectives may bring everyone to a common point.

Project Management –

When using the MoSCoW technique it would be useful if I included Could Have and Won&#39;t Have tasks. Not only would it dictate what the application may have looked like or the ideas for a better application, however it could be a start point for a future project or an update on the current application.

Other improvements –

- Incorporate a login area allowing personalisation for user
- Include a favourites tab for fans to select their favourite promotions or fighters
- Insert a events tab, allowing users to be notified about upcoming fights
- Include logos and pictures so users can put a face to the name of the fighter and promotion
- Have more user stories. Including a lot more user stories enable to view more perspectives from more users as users will all have different needs.

### Authors

Mahammed Kassam

### Acknowledgements

Many thanks go to the trainer, Earl Gray, for all his help, guidance, and patience. The cohort of 22MarEnable1 deserve to be acknowledged for their support and friendly demeanour. Not forgetting Leon Robinson for taking lead on a few sessions at short notice and also Harry Volker for being available to answer questions .

Thanks go to getbootstrap for their navbar.
