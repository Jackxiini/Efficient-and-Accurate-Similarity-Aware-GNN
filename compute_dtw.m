function [dtw_mat, time1] = compute_dtw(data_name)
coffee_train = load(['UCR/' data_name '/' data_name '_TRAIN.tsv']);
coffee_test = load(['UCR/' data_name '/' data_name '_TEST.tsv']);

train_label = coffee_train(:,1);
test_label = coffee_test(:,1);
coffee_train = coffee_train(:,2:end);
coffee_test = coffee_test(:,2:end);

instance_sum = size(coffee_train,1)+size(coffee_test,1);

data=[coffee_train; coffee_test];

r = min(size(coffee_train,2),100);
disp(r);


time1 = 0;
tic
% compute DTW mtx. 
dtw_mat = zeros(instance_sum, instance_sum);
for i=1:instance_sum
    for j=1:instance_sum
    dtw_mat(i,j)=dtw(data(i,:), data(j,:),r);
    end 
end
time1= toc;
disp([data_name,' time: ' num2str(time1)])
writematrix(dtw_mat,['UCR/' data_name, '/dtw_mat.txt'],'Delimiter',',')
save(['UCR/' data_name, '/dtw_mat.mat'], 'time1','dtw_mat', '-v7.3')
save(['UCR/' data_name, '/timetaken.mat'], 'time1')
