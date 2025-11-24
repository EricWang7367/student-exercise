# Exercise 4: Mini hackathon

This exercise should be done in pairs (or larger groups if you'd prefer).

Choose one of the following requirements to implement, following the same process as before.  At the end of the
session you will play back to the group which requirement you chose, your considerations during testing,
any decisions you made for the implementation (and why), and maybe even do a live demo of the feature!


## Option 1: Adding additional attributes to the existing entities

Registers and entries only have a `name` currently which isn't hugely useful.  Your task is to come up with two or three 
additional attributes for `register` and `entry` (or both), write some high level requirements/acceptance criteria, and 
create the corresponding tests/implementation.
Things to consider:
* How the attributes should be modelled in the database
* Input validation when creating/updating the attributes
* Suitable UI components (text, dropdown, radio, etc)

## Option 2: Add and manage 'parties'

A `party` is a person or organisation that has an interest in or may be referred to on a particular entry on a register.
Your task is to implement the concept of a `party` with a `name` and `type` attribute, write some high level 
requirements/acceptance criteria, and create the corresponding tests/implementation.
Things to consider:
* How a party should be modelled in the database (including its relationship to `entry`)
* Input validation when creating/updating a `party`
* User journey (UI/UX) for creating, viewing, etc
* Can a party be linked to multiple entries?


## Option 3: Import/Export

We need to be able to import/export registers to allow them to be moved/migrated between systems.  Your task is to write 
some high level requirements/acceptance criteria for an import/export feature, and create the corresponding tests/implementation.
Things to consider:
* How will entity relationships be modelled in the export file?
* What happens if you try to import a register/entry that already exists?
* Will importing an existing register/entry fail or overwrite?
