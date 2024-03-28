data_names = {'StarLightCurves'};

time_vec = [];
for i = 1:length(data_names)
    data_name = data_names{i};
    [dtw_mat, time1] = compute_dtw(data_name);
    time_vec(i) = time1;
    disp(data_name)
end

