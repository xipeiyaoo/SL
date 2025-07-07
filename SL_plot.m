clear,clc

%% bar 图
% 定义参数
n_groups = 2;       % 4个被试间变量组
n_levels = 3;       % 3个被试内水平
n_subjects_per_group = 26;    % 总被试数

% ========== 步骤1：计算均值和标准误 ==========
means = zeros(n_groups, n_levels);
errors = zeros(n_groups, n_levels);

for group = 1:n_groups
    % 提取当前组的3列数据（例如组1：列1-3）
    cols = (group-1)*n_levels + 1 : group*n_levels;
    group_data = data(:, cols);
    
    % 计算均值和标准误（忽略NaN）
    means(group,:) = nanmean(group_data, 1);
    errors(group,:) = nanstd(group_data)/sqrt(size(group_data,1));
end

% ========== 步骤2：生成自定义坐标轴位置 ==========
% 控制间距参数
intra_group_gap = 0.18;    % 组内柱子间距（值越小间距越大）
inter_group_gap = 0.6;     % 组间整体间距（值越大间距越大）

% 生成位置矩阵
x = zeros(n_groups, n_levels);
for group = 1:n_groups
    base_pos = (group-1)*(n_levels + inter_group_gap);
    x(group,:) = base_pos + (1:n_levels);
end

% ========== 步骤3：绘制柱状图 ==========
figure('Position', [100,100,780,500]) % 设置画布大小
hold on

% 自定义颜色（每个水平一个颜色）
% colors = [241 130 160;   % 水平1：粉色
%           126 118 163;   % 水平2：紫色
%           72 179 204]/255;  % 水平3：蓝色

% colors = [166 204 237;   % 水平1：浅蓝色
%           184 195 228;   % 水平2：浅紫色
%           127 191 165]/255;  % 水平3：浅绿色

% colors = [192 80 78;   % 水平1：红色
%           229 185 184;   % 水平2：粉色
%           247 150 71]/255;  % 水平3：橙色
 
colors = [136 179 214;   % 水平1：蓝色
          142 198 163;   % 水平2：绿色
          229 154 155]/255;  % 水平3：粉色

% colors = [149 220 232;   % 水平1：蓝色
%           186 220 148;   % 水平2：绿色
%           215 202 227]/255;  % 水平3：粉色

% 绘制每个水平的柱子
for level = 1:n_levels
    bar(x(:,level), means(:,level),...
        'BarWidth', intra_group_gap,...
        'FaceColor', colors(level,:),...
        'EdgeColor', 'k',...
        'LineWidth', 2);
end

% ========== 步骤4：添加误差棒 ==========
for group = 1:n_groups
    for level = 1:n_levels
        errorbar(x(group,level),...
                means(group,level),...
                errors(group,level),...
                'k',...
                'LineWidth', 2,...
                'CapSize', 5);
    end
end

% ========== 步骤5：美化图形 ==========
% 设置坐标轴
set(gca, 'XTick', mean(x,2),...          % 将刻度放在每组中心
         'FontSize', 12,...
         'LineWidth', 3)

xlim([min(x(:))-1, max(x(:))+1])
ylim([900,1300])

set(gca,'Box','off') ;
set(gca,'linewidth',3)
set(gca,'tickdir','out') 
set(gca,'YTick',900:200:1300)
set(gca,'xticklabel',[])
set(gca,'yticklabel',[])
% % 添加图例
% legend({'Level1','Level2','Level3'},...
%        'Location', 'northeast',...
%        'FontSize', 11)

% 添加标签
% xlabel('Between-Subject Groups', 'FontSize', 13)
% ylabel('Reaction Time (ms)', 'FontSize', 13)
% title('Reaction Time by Experimental Condition', 'FontSize', 14)

% 调整坐标范围

% hold off





%% 折线图
% 假设你的数据是一个4列的矩阵，每列代表一组数据
% 每列有多个观测值，这里我们假设每列有5个观测值
% 计算每列的平均值和标准误差（或标准差）
mean_values = mean(data);
std_errors = std(data) / sqrt(size(data, 1)); % 标准误差

% 定义x轴的位置
x = 1:4;

% 绘制折线图
figure('Position', [100,100,550,500]) 
hold on;

%color1=[231,98,84]/255;%红
%color2=[50, 200, 200]/255;%蓝
%color2=[176, 164, 227]/255;%紫
color2=[144, 121, 173]/255;%深一点的紫
%color2=[236, 109, 113]/255;%真朱
% 添加误差线
errorbar(x, mean_values, std_errors, 'o', 'MarkerSize', 6, 'Color', 'black', 'LineStyle', 'none','LineWidth',2,'MarkerEdgeColor','none');

% 绘制前两列的线
plot(x(1:2), mean_values(1:2), '-o', 'LineWidth', 3, 'MarkerSize', 6, 'MarkerFaceColor',color2,'MarkerEdgeColor',color2,'Color',color2);

% 绘制后两列的线
plot(x(3:4), mean_values(3:4), '-o', 'LineWidth', 3, 'MarkerSize', 6, 'MarkerFaceColor',color2,'MarkerEdgeColor',color2,'Color',color2);


% 设置x轴刻度标签
xlim([0.5,2.5])
xticks(1:4);
set(gca,'xticklabel',[])
yticks(20:20:60);
set(gca,'yticklabel',[])
set(gca,'Box','off') ;
set(gca,'linewidth',3)
set(gca,'tickdir','out') 
%xticklabels({'1', '2', '3', '4'});

% % 添加标题和标签
% title('Four Groups with Two Lines');
% xlabel('Groups');
% ylabel('Mean Values');



%% 相关那个散点图

% ========== 计算相关性与拟合线 ==========
dif_cap=data(:,1);
dif_learn=data(:,2);

[pearson_r, pearson_p] = corr(dif_cap, dif_learn, 'Type','Spearman');

% 线性拟合（最小二乘法）
p = polyfit(dif_cap, dif_learn, 1);  % 1次多项式拟合
fit_line = polyval(p, [min(dif_cap), max(dif_cap)]);

% ========== 绘制散点图 ==========
figure('Position', [100 100 500 500])
scatter(dif_cap, dif_learn, 70, 'filled',...
    'MarkerFaceColor', [246, 191, 188]/255,...
    'MarkerEdgeColor', [246, 191, 188]/255,...
    'LineWidth', 1)
hold on

% 绘制拟合线
plot([min(dif_cap), max(dif_cap)], fit_line,...
    'Color', [238, 130, 124]/255,...
    'LineWidth', 2.5)

% ========== 添加统计标注 ==========
% text_x = min(dif_cap) + 0.7*(max(dif_cap)-min(dif_cap));
% text_y = min(dif_learn) + 0.85*(max(dif_learn)-min(dif_learn));
% 
% text(text_x, text_y,...
%     sprintf('Pearson r = %.2f (p = %.3f)',...
%     pearson_r, pearson_p),...
%     'FontSize', 12,...
%     'BackgroundColor', [1 1 1 0.8],...
%     'EdgeColor', 'k')

% ========== 美化图形 ==========
set(gca, 'FontSize', 12, 'LineWidth', 1.2)
set(gca,'yticklabel',[],'xticklabel',[])

set(gca,'Box','off','XAxisLocation','origin','YAxisLocation','origin') ;
set(gca,'linewidth',2)
set(gca,'tickdir','out') 

% xlabel('Difference in Capacity (dif_{cap})', 'FontSize', 14)
% ylabel('Difference in Learning (dif_{learn})', 'FontSize', 14)
% title('Correlation Between Capacity and Learning Differences', 'FontSize', 16)
% grid on
% axis tight


% 添加图例
legend({'Data Points', sprintf('Linear Fit: y = %.2fx + %.2f', p(1), p(2))},...
    'Location', 'best',...
    'FontSize', 12)





%% 画散点bar
% 假设 X 是一个 N×6 的矩阵，每列代表一组数据
% 生成示例数据（替换为你的实际数据）
rng(1);
X =data(:,1:6); % 6列数据，前三列与后三列颜色配对

% --- 参数设置 ---
% 1. 定义颜色配对：前三列与后三列颜色相同
colors = [
    0.2 0.6 0.8;   % 第1列颜色（与第4列相同）
    0.8 0.4 0.2;   % 第2列颜色（与第5列相同）
    0.4 0.8 0.4;   % 第3列颜色（与第6列相同）
    0.2 0.6 0.8;   % 第4列
    0.8 0.4 0.2;   % 第5列
    0.4 0.8 0.4    % 第6列
];

% 2. 定义X轴位置：前三列紧凑（1,2,3），后三列紧凑（5,6,7）
x_positions = [1, 2, 3, 5, 6, 7]; % 中间留出间距

% 3. 抖动参数
jitterWidth = 0.0; % 抖动幅度
markerSize = 80;     % 散点大小

% --- 计算均值和SEM ---
mean_y = mean(X, 1);        % 行方向均值（每列）
sem = std(X, 0, 1) ./ sqrt(size(X, 1)); % 标准误差

% --- 绘制图形 ---
figure('Position', [100,100,780,500]) 
hold on;

% 绘制散点（带抖动）
for i = 1:6
    % 生成抖动后的X坐标
    x_jitter = x_positions(i) + jitterWidth*(rand(size(X(:,i))) - 0.5);
    
    % 绘制散点
    scatter(x_jitter, X(:,i), markerSize, ...
        'MarkerFaceColor', colors(i,:), ...
        'MarkerEdgeColor', 'k', ...
        'MarkerFaceAlpha', 0.6, ...
        'MarkerEdgeAlpha', 0.3);
end

% 绘制均值和SEM误差条
errorbar(x_positions, mean_y, sem, 'LineStyle', 'none', ...
    'Color', [0.2,0.2,0.2], 'LineWidth', 1.5, 'CapSize', 8);
plot(x_positions, mean_y, '_','Color',[0.2,0.2,0.2], 'MarkerSize', 16, 'LineWidth', 2);

% --- 图形修饰 ---
set(gca, 'FontSize', 12, 'LineWidth', 1.5, 'XTick', [2,6],'XTickLabel',[], ...
    'Xlim', [0.5, 7.5], 'Ylim', [min(X(:))-1, max(X(:))+1]);
%ylabel('Value');
%title('分组散点图（均值±SEM）');
set(gca,'Box','off') ;
set(gca,'linewidth',3)
set(gca,'tickdir','out') 

% 添加图例（可选）
% legend({'Group 1-4', 'Group 2-5', 'Group 3-6'}, ...
  %  'Location', 'northwest', 'Color', [0.95 0.95 0.95]);

hold off;




%% 随block变化的折线图
% 横轴标签（block1-6）
blocks = 1:6;

% 数据矩阵（4行对应4个条件，6列对应block1-6）
data = [...
    1262.910675 1169.847061 1104.689979 1099.447339 1042.339866 1045.954096;  % 31_base
    1324.639496 1234.030901 1161.062486 1125.868322 1103.414276 1064.321283;  % 31_sali
    1347.444119 1258.350055 1204.439894 1157.41505  1127.783265 1096.947659;  % 41_base
    1267.48613  1149.348048 1073.061523 1016.648373  996.6330711 986.3050477]; % 41_sali

% 条件名称
% conditions = {'31\_base', '31\_sali', '41\_base', '41\_sali'};

%% 颜色定义（RGB格式）
colors = [...
    0 0.4470 0.7410;   % 蓝色
    0.8500 0.3250 0.0980; % 橙色
    0.9290 0.6940 0.1250; % 黄色
    0.4940 0.1840 0.5560]; % 紫色

%% 绘图设置
figure('Position', [100,100,780,500]) % 设置窗口大小
hold on; % 保持绘图区域

% 绘制每条折线
for i = 1:2
    plot(blocks, data(i,:),...
        'LineWidth', 3,...
        'Color', colors(i,:),...
        'Marker', 'o',...
        'MarkerSize', 8,...
        'MarkerFaceColor', colors(i,:));
end

%% 图表美化
% 坐标轴设置
set(gca, 'FontSize', 12, 'LineWidth', 3);
% xlabel('Block Number', 'FontSize', 14);
% ylabel('Measurement Value', 'FontSize', 14);
xticks(1:6);
% xticklabels({'Block1','Block2','Block3','Block4','Block5','Block6'});
xlim([0.5 6.5]);
grid off;
set(gca,'tickdir','out') 
set( gca,'YTick', [950:200:1350],'YTickLabel',[]);
% % 图例设置
% legend(conditions,...
%     'Location', 'best',...
%     'FontSize', 12,...
%     'Interpreter', 'none'); % 防止下划线被识别为LaTeX
% 
% % 标题（可选）
% title('Performance Across Blocks', 'FontSize', 16);




%% 画学习效果个体差异散点图
% 假设条件1数据：26个被试 × 6个block（示例用随机数生成）
cond1_data = 500 + 200*rand(26,6); % 26个被试，6个block
% 假设条件2数据：另一个26个被试 × 6个block
cond2_data = 600 + 150*rand(26,6); % 26个被试，6个block

figure('Position', [100 100 900 600]) % 设置窗口大小
hold on;

% 定义颜色方案
colors = [ 0 0.4470 0.7410;   % 蓝色
    0.8500 0.3250 0.0980]; % 橙色;  

% 定义block坐标
blocks = 1:6;

%% 绘制条件1数据（带个体连线）
for subj = 1:26
    % 绘制散点
    scatter(blocks, cond1_data(subj,:),...
        60, ... % 点大小
        'MarkerFaceColor', colors(1,:),...
        'MarkerEdgeColor', colors(1,:),...
        'MarkerFaceAlpha', 0.4,...
        'MarkerEdgeAlpha', 0.6);
    
    % 连接同被试的block
    plot(blocks, cond1_data(subj,:),...
        'Color', [colors(1,:) 0.3],... % 带透明度
        'LineWidth', 1.2);
end

%% 绘制条件2数据（带个体连线）
for subj = 1:26
    scatter(blocks, cond2_data(subj,:),...
        60,...
        'MarkerFaceColor', colors(2,:),...
        'MarkerEdgeColor', colors(2,:),...
        'MarkerFaceAlpha', 0.4,...
        'MarkerEdgeAlpha', 0.6);
    
    plot(blocks, cond2_data(subj,:),...
        'Color', [colors(2,:) 0.3],...
        'LineWidth', 1.2);
end

%% 添加平均趋势线（可选）
plot(blocks, mean(cond1_data),...
    'Color', colors(1,:),...
    'LineWidth', 3,...
    'LineStyle', '-');

plot(blocks, mean(cond2_data),...
    'Color', colors(2,:),...
    'LineWidth', 3,...
    'LineStyle', '-');

%% 图表美化
set(gca, 'FontSize', 12, 'LineWidth', 3);
% xlabel('Block Number', 'FontSize', 14);
% ylabel('Reaction Time (ms)', 'FontSize', 14);
xticks(1:6);
% xticklabels({'Block1','Block2','Block3','Block4','Block5','Block6'});
xlim([0.8 6.2]);
grid off;
set(gca,'tickdir','out') 
% % 自定义图例
% h = zeros(2,1);
% h(1) = plot(NaN,NaN,'o-','Color',colors(1,:),'MarkerFaceColor',colors(1,:));
% h(2) = plot(NaN,NaN,'o-','Color',colors(2,:),'MarkerFaceColor',colors(2,:));
% legend(h, {'Condition 1', 'Condition 2'},...
%     'Location', 'best',...
%     'FontSize',12);





%% 单个条件图
% 假设条件1数据：26个被试 × 6个block（示例用随机数生成）
cond1_data = 500 + 200*rand(26,6); % 26个被试，6个block
% 假设条件2数据：另一个26个被试 × 6个block
%cond2_data = 600 + 150*rand(26,6); % 26个被试，6个block

figure('Position', [100 100 900 600]) % 设置窗口大小
hold on;

% 定义颜色方案
%colors = [0 0.4470 0.7410]; % 蓝色 
colors = [0.8500 0.3250 0.0980]; % 蓝色 
% 定义block坐标
blocks = 1:6;

%% 绘制条件1数据（带个体连线）
for subj = 1:26
    % 绘制散点
    scatter(blocks, cond1_data(subj,:),...
        60, ... % 点大小
        'MarkerFaceColor', colors(1,:),...
        'MarkerEdgeColor', colors(1,:),...
        'MarkerFaceAlpha', 0.4,...
        'MarkerEdgeAlpha', 0.6);
    
    % 连接同被试的block
    plot(blocks, cond1_data(subj,:),...
        'Color', [colors(1,:) 0.3],... % 带透明度
        'LineWidth', 1.2);
end


%% 添加平均趋势线（可选）
plot(blocks, mean(cond1_data),...
    'Color', colors(1,:),...
    'LineWidth', 3,...
    'LineStyle', '-');

% plot(blocks, mean(cond2_data),...
%     'Color', colors(2,:),...
%     'LineWidth', 3,...
%     'LineStyle', '-');

%% 图表美化
set(gca, 'FontSize', 12, 'LineWidth', 3);
% xlabel('Block Number', 'FontSize', 14);
% ylabel('Reaction Time (ms)', 'FontSize', 14);
xticks(1:6);
% xticklabels({'Block1','Block2','Block3','Block4','Block5','Block6'});
xticklabels({});
yticklabels({});
xlim([0.8 6.2]);
grid off;
set(gca,'tickdir','out') 




%% 画重复条件反应时
% 假设你的数据是一个4列的矩阵，每列代表一组数据
% 每列有多个观测值，这里我们假设每列有5个观测值
% 计算每列的平均值和标准误差（或标准差）
mean_values = mean(data);
std_errors = std(data) / sqrt(size(data, 1)); % 标准误差

% 定义x轴的位置
x = 1:4;

% 绘制折线图
figure('Position', [100,100,550,500]) 
hold on;

%color1=[231,98,84]/255;%红
%color2=[50, 200, 200]/255;%蓝
%color2=[176, 164, 227]/255;%紫
%color2=[144, 121, 173]/255;%深一点的紫
%color2=[236, 109, 113]/255;%真朱
color1=[138,188,209]/255;%hong
color2=[108,169,132]/255;%lv
% 添加误差线
errorbar(x(1:2), mean_values(1:2), std_errors(1:2), 'o', 'MarkerSize', 6, 'Color', 'black', 'LineStyle', 'none','LineWidth',2,'MarkerEdgeColor','none');

errorbar(x(1:2), mean_values(3:4), std_errors(3:4), 'o', 'MarkerSize', 6, 'Color', 'black', 'LineStyle', 'none','LineWidth',2,'MarkerEdgeColor','none');

% 绘制前两列的线
plot(x(1:2), mean_values(1:2), '-o', 'LineWidth', 3, 'MarkerSize', 6, 'MarkerFaceColor',color1,'MarkerEdgeColor',color1,'Color',color1);


% 绘制后两列的线
plot(x(1:2), mean_values(3:4), '-o', 'LineWidth', 3, 'MarkerSize', 6, 'MarkerFaceColor',color2,'MarkerEdgeColor',color2,'Color',color2);


% 设置x轴刻度标签
xlim([0.5,2.5])
xticks(1:3);
set(gca,'xticklabel',[])
%yticks(20:20:60);
set(gca,'yticklabel',[])
set(gca,'Box','off') ;
set(gca,'linewidth',3)
set(gca,'tickdir','out') 
%xticklabels({'1', '2', '3', '4'});



%% 

% 定义颜色 (RGB值)
colors = [92 179 204;   % high - 蓝绿色
          126 118 163;   % low - 橙红色
          241 130 160]/255;  % no - 绿色

% 创建图形
figure('Position', [100, 100, 780, 500]);
hold on;

% 设置主组位置和间距参数
main_group_positions = [1.5, 3.5];  % 增大主组间距 (standard和large之间)
sub_group_spacing = 0.4;       % 减小子组间距 (high/low/no之间)
bar_width = 0.3;                % 条形宽度

% 计算所有条形的精确位置
all_positions = zeros(2, 3);  % 存储每个条形的x位置

% 为每个条件(high/low/no)绘制柱状图和误差线
for cond = 1:3
    for group = 1:2
        % 计算当前条形位置
        x_pos = main_group_positions(group) + (cond)*sub_group_spacing;
        all_positions(group, cond) = x_pos;
        
        % 绘制条形
        bar(x_pos, mean(group, cond), bar_width, ...
            'FaceColor', colors(cond, :), ...
            'EdgeColor', 'k', ...
            'LineWidth', 1.5);
        
        % 添加误差线
        errorbar(x_pos, mean(group, cond), std(group, cond), ...
                 'k', 'LineStyle', 'none', 'LineWidth', 1.5, ...
                 'CapSize', 8);
    end
end

% 设置坐标轴和标签
xlim([1, 5]);
ylim([900, 1300]);
set(gca,'xticklabel',[])
%yticks(20:20:60);
set(gca,'yticklabel',[])
set(gca,'Box','off') ;
set(gca,'linewidth',3)
set(gca,'tickdir','out') 