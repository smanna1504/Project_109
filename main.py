import pandas as pd
import csv
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv('data.csv')

# The below code deals with the 'math score' parameter only. The same can be done with the other parameters as well simply by changing the names
 
math_score_list=df['math score'].to_list()

mean=statistics.mean(math_score_list)
median=statistics.median(math_score_list)
mode=statistics.mode(math_score_list)
std_deviation=statistics.stdev(math_score_list)

print('Mean, Median & Mode for Math Scores are {}, {} & {} respectively'.format(mean,median,mode))

first_std_deviation_start,first_std_deviation_end=mean-std_deviation,mean+std_deviation
second_std_deviation_start,second_std_deviation_end=mean-(2*std_deviation),mean+(std_deviation*2)
third_std_deviation_start,third_std_deviation_end=mean-(3*std_deviation),mean+(std_deviation*3)



list1=[result for result in math_score_list if result>first_std_deviation_start and result<first_std_deviation_end]
list2=[result for result in math_score_list if result>second_std_deviation_start and result<second_std_deviation_end]
list3=[result for result in math_score_list if result>third_std_deviation_start and result<third_std_deviation_end]


print('{}% of data is b/w 1st std deviation '.format(len(list1)*100/len(math_score_list)))
print('{}% of data is b/w 2nd std deviation '.format(len(list2)*100/len(math_score_list)))
print('{}% of data is b/w 3rd std deviation '.format(len(list3)*100/len(math_score_list)))

fig=ff.create_distplot([math_score_list],['math score'], show_hist=False)

fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode="lines",name="1st STANDARD DEVIATION"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="1st STANDARD DEVIATION"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode="lines",name="2nd STANDARD DEVIATION"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="2nd STANDARD DEVIATION"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start],y=[0,0.17],mode="lines",name="3rd STANDARD DEVIATION"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode="lines",name="3rd STANDARD DEVIATION"))

fig.show()