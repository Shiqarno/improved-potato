# improved-potato
Trying to build a model for forex trading

This project aims to create a model for automated forex trading

In fact, these are several models, each for its own purpose

The classic approach to market analysis is the regression problem. "Here's a series of prices, tell me the next one"

This project takes a different approach. Looking for patterns in which the market tends to behave in a certain way.
If we have found one, we can say with a high probability where the market will go.
This is a classification task

So we need 3 models:
- a model that will determine that a given market point belongs to the classes that we are looking for (codename `mushroom`)
- a model that will determine if a given market point is suitable for entry (codename `potato`)
- a model that will determine whether it is already possible to fix profits, fix losses, or you can still wait for better options (codename `butter`)

Let's rock!