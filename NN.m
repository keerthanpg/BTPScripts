A=importdata('featuresarraytrain.txt');
B=importdata('emotionarraytrain.txt');
A=transpose(A);
B=transpose(B);
inputs=A(1:14,180);
targets=B(1:8,180);

for n = 151:300
net = fitnet(n,'trainrp');
net.divideParam.trainRatio = 70/100;
net.divideParam.valRatio = 15/100;
net.divideParam.testRatio = 15/100;
% Setup Division of Data for Training, Validation, Testing

net=train(net, A, B);
y = net(A);
c(n,1)=n;
c(n,2)= perform(net,y,B);
end
%outputs = net(inputs);
%errors = gsubtract(targets,outputs);
%performance = perform(net,targets,outputs)
%targets
%outputsc
%net.LW{2,1}
plot(c(:,1),c(:,2))
