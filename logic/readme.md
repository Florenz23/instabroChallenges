Instabro Logic Challenge

languages:
python, postgresql

libaries to use:
sqlalchemie

instruction:
https://docs.google.com/document/d/1_LBmvEF_P7XO75PEerewZvTCbbMynL4klal3EFwZjo4/edit


code patterns:

Coding Requirements

general:
  maximum characters of column : 80 (open this with editor for examle)
  example:
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Naming:
  constants: follow_amount
  variables: followAmount
  functions: setFollowAmount

functions:
  maximum characters of column : 80
  maximum lines: 10-15
  a method should do one thing and only one thing.
    theory:
      It's not about lines of code. As Steve Mcconnell and Bob Martin say (two pretty good references on coding best practices), a method should do one thing and only one thing. However many lines of code it takes to do that one thing is how many lines it should have. If that "one thing" can be broken into smaller things, each of those should have a method.

      Good clues your method is doing more than one thing:

      More than one level of indention in a method (indicates too many logic branches to only be doing one thing)
      "Paragraph Breaks" - whitespace between logical groups of code indicate the method is doing more than one thing
      Just to name a few. Bob Martin also says to keep it around 10. Personally I usually try to shoot for 10. If it starts getting close to 20, that's a mental flag to pay closer attention to that method. But ultimately, LoC is a bad metric for pretty much anything. It is only a helpful indicator that can potentially point to the real issue.
