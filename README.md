# ad_image
ad_image recognition

try to identify ad imgage from the web page.
did a lot of experiments; different combinition of :

- removed instances with missing values
- normalisation
- 3 feature selection method : chi-squrare test / CFS / classifier subset evaluator
- 7 rebalancing percentage: i have used SMOTE to rebalance the data, to tackle/mitigate class imbalance
- 4 algos: Naive Bayes, Decision tree, random forest, SVM
- also tried bagging and boosting techniques on the best performance ones

The best two tests from NB and SVM are selected to do bagging and boosting test.

Defined a weighted average score to evaluate the performance, 
apart from accuracy metrics, it also consider test time;
because the background is the project is used for a web-browsing tool. if it takes too much time running the algos, before loading the page the tool will be useless and annoying. 

Final Report
https://drive.google.com/file/d/1dsV_fVEZ2p13onF7EF6rUNE26VnkRzyG/view?usp=sharing
