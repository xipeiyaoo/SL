/******************* 
 * Sl_Base_41 Test *
 *******************/


// store info about the experiment session:
let expName = 'SL_base_41';  // from the Builder filename that created this script
let expInfo = {'participant': '001'};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'pix',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instrRoutineBegin());
flowScheduler.add(instrRoutineEachFrame());
flowScheduler.add(instrRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(formal_cueRoutineBegin());
flowScheduler.add(formal_cueRoutineEachFrame());
flowScheduler.add(formal_cueRoutineEnd());
const trials_3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_3LoopBegin(trials_3LoopScheduler));
flowScheduler.add(trials_3LoopScheduler);
flowScheduler.add(trials_3LoopEnd);
flowScheduler.add(endRoutineBegin());
flowScheduler.add(endRoutineEachFrame());
flowScheduler.add(endRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
async function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.2.3';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var instrClock;
var text;
var key_resp;
var fixClock;
var fix_circle;
var trialClock;
var fixation;
var loc1_shape;
var loc1_line;
var loc2_shape;
var loc2_line;
var loc3_shape;
var loc3_line;
var loc4_shape;
var loc4_line;
var loc5_shape;
var loc5_line;
var loc6_shape;
var loc6_line;
var loc7_shape;
var loc7_line;
var loc8_shape;
var loc8_line;
var resp;
var block_num;
var circle_vertices;
var theta;
var x;
var y;
var green;
var red;
var a;
var diamond_vertices;
var b;
var hori_start;
var hori_end;
var vert_start;
var vert_end;
var c;
var d;
var loc1;
var loc2;
var loc3;
var loc4;
var loc5;
var loc6;
var loc7;
var loc8;
var locs;
var high_prob_loc;
var low_prob_locs;
var distractor_locs;
var tar_only_locs;
var shape;
var distractor;
var distractor_new;
var detection;
var base_trial_count;
var repeat_times;
var trial_list_new;
var trial;
var j;
var k;
var filtered_locs;
var n;
var random_index;
var tar_both_loc;
var new_trial;
var dis_loc_fake;
var current_trial;
var feedbackClock;
var text_4;
var itiClock;
var iti_blank;
var formal_cueClock;
var text_2;
var key_resp_2;
var break_3Clock;
var text_3;
var key_resp_3;
var endClock;
var end_2;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "instr"
  instrClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '欢迎来到本次实验\n\n接下来屏幕上会出现若干形状\n您的任务是找到这些形状中的独特形状（如圆形中的菱形），\n并判断该独特形状内线段的方向，\n如果线段是竖直的，请按“上”键，如果线段是水平的，请按“左”键。\n首先呈现练习试次，随后开始正式实验。\n\n明白后请按空格键开始。',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 30.0,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fix"
  fixClock = new util.Clock();
  fix_circle = new visual.Polygon ({
    win: psychoJS.window, name: 'fix_circle', 
    edges: 9999, size:[20, 20],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  fixation = new visual.Polygon ({
    win: psychoJS.window, name: 'fixation', 
    edges: 9999, size:[20, 20],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  loc1_shape = new visual.Rect ({
    win: psychoJS.window, name: 'loc1_shape', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 45.0, pos: [150, 0],
    lineWidth: 2.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('[0,0,0]'),
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  loc1_line = new visual.ShapeStim ({
    win: psychoJS.window, name: 'loc1_line', 
    vertices: [[-[1, 1][0]/2.0, 0], [+[1, 1][0]/2.0, 0]],
    ori: 0.0, pos: [150, 0],
    lineWidth: 2.0, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  loc2_shape = new visual.ShapeStim ({
    win: psychoJS.window, name: 'loc2_shape', 
    vertices: [[-[2, 2][0]/2.0, -[2, 2][1]/2.0], [+[2, 2][0]/2.0, -[2, 2][1]/2.0], [0, [2, 2][1]/2.0]],
    ori: 45.0, pos: [106, 106],
    lineWidth: 2.0, lineColor: new util.Color('red'),
    fillColor: new util.Color('[0,0,0]'),
    opacity: undefined, depth: -3, interpolate: true,
  });
  
  loc2_line = new visual.ShapeStim ({
    win: psychoJS.window, name: 'loc2_line', 
    vertices: [[-[1, 1][0]/2.0, 0], [+[1, 1][0]/2.0, 0]],
    ori: 0.0, pos: [106, 106],
    lineWidth: 2.0, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: undefined, depth: -4, interpolate: true,
  });
  
  loc3_shape = new visual.ShapeStim ({
    win: psychoJS.window, name: 'loc3_shape', 
    vertices: [[-[2, 2][0]/2.0, -[2, 2][1]/2.0], [+[2, 2][0]/2.0, -[2, 2][1]/2.0], [0, [2, 2][1]/2.0]],
    ori: 45.0, pos: [0, 150],
    lineWidth: 2.0, lineColor: new util.Color('red'),
    fillColor: new util.Color('[0,0,0]'),
    opacity: undefined, depth: -5, interpolate: true,
  });
  
  loc3_line = new visual.ShapeStim ({
    win: psychoJS.window, name: 'loc3_line', 
    vertices: [[-[1, 1][0]/2.0, 0], [+[1, 1][0]/2.0, 0]],
    ori: 0.0, pos: [0, 150],
    lineWidth: 2.0, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: undefined, depth: -6, interpolate: true,
  });
  
  loc4_shape = new visual.ShapeStim ({
    win: psychoJS.window, name: 'loc4_shape', 
    vertices: [[-[2, 2][0]/2.0, -[2, 2][1]/2.0], [+[2, 2][0]/2.0, -[2, 2][1]/2.0], [0, [2, 2][1]/2.0]],
    ori: 45.0, pos: [(- 106), 106],
    lineWidth: 2.0, lineColor: new util.Color('red'),
    fillColor: new util.Color('[0,0,0]'),
    opacity: undefined, depth: -7, interpolate: true,
  });
  
  loc4_line = new visual.ShapeStim ({
    win: psychoJS.window, name: 'loc4_line', 
    vertices: [[-[1, 1][0]/2.0, 0], [+[1, 1][0]/2.0, 0]],
    ori: 0.0, pos: [(- 106), 106],
    lineWidth: 2.0, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: undefined, depth: -8, interpolate: true,
  });
  
  loc5_shape = new visual.ShapeStim ({
    win: psychoJS.window, name: 'loc5_shape', 
    vertices: [[-[2, 2][0]/2.0, -[2, 2][1]/2.0], [+[2, 2][0]/2.0, -[2, 2][1]/2.0], [0, [2, 2][1]/2.0]],
    ori: 45.0, pos: [(- 150), 0],
    lineWidth: 2.0, lineColor: new util.Color('red'),
    fillColor: new util.Color('[0,0,0]'),
    opacity: undefined, depth: -9, interpolate: true,
  });
  
  loc5_line = new visual.ShapeStim ({
    win: psychoJS.window, name: 'loc5_line', 
    vertices: [[-[1, 1][0]/2.0, 0], [+[1, 1][0]/2.0, 0]],
    ori: 0.0, pos: [(- 150), 0],
    lineWidth: 2.0, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: undefined, depth: -10, interpolate: true,
  });
  
  loc6_shape = new visual.ShapeStim ({
    win: psychoJS.window, name: 'loc6_shape', 
    vertices: [[-[2, 2][0]/2.0, -[2, 2][1]/2.0], [+[2, 2][0]/2.0, -[2, 2][1]/2.0], [0, [2, 2][1]/2.0]],
    ori: 45.0, pos: [(- 106), (- 106)],
    lineWidth: 2.0, lineColor: new util.Color('red'),
    fillColor: new util.Color('[0,0,0]'),
    opacity: undefined, depth: -11, interpolate: true,
  });
  
  loc6_line = new visual.ShapeStim ({
    win: psychoJS.window, name: 'loc6_line', 
    vertices: [[-[1, 1][0]/2.0, 0], [+[1, 1][0]/2.0, 0]],
    ori: 0.0, pos: [(- 106), (- 106)],
    lineWidth: 2.0, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: undefined, depth: -12, interpolate: true,
  });
  
  loc7_shape = new visual.ShapeStim ({
    win: psychoJS.window, name: 'loc7_shape', 
    vertices: [[-[2, 2][0]/2.0, -[2, 2][1]/2.0], [+[2, 2][0]/2.0, -[2, 2][1]/2.0], [0, [2, 2][1]/2.0]],
    ori: 45.0, pos: [0, (- 150)],
    lineWidth: 2.0, lineColor: new util.Color('red'),
    fillColor: new util.Color('[0,0,0]'),
    opacity: undefined, depth: -13, interpolate: true,
  });
  
  loc7_line = new visual.ShapeStim ({
    win: psychoJS.window, name: 'loc7_line', 
    vertices: [[-[1, 1][0]/2.0, 0], [+[1, 1][0]/2.0, 0]],
    ori: 0.0, pos: [0, (- 150)],
    lineWidth: 2.0, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: undefined, depth: -14, interpolate: true,
  });
  
  loc8_shape = new visual.ShapeStim ({
    win: psychoJS.window, name: 'loc8_shape', 
    vertices: [[-[2, 2][0]/2.0, -[2, 2][1]/2.0], [+[2, 2][0]/2.0, -[2, 2][1]/2.0], [0, [2, 2][1]/2.0]],
    ori: 45.0, pos: [106, (- 106)],
    lineWidth: 2.0, lineColor: new util.Color('red'),
    fillColor: new util.Color('[0,0,0]'),
    opacity: undefined, depth: -15, interpolate: true,
  });
  
  loc8_line = new visual.ShapeStim ({
    win: psychoJS.window, name: 'loc8_line', 
    vertices: [[-[1, 1][0]/2.0, 0], [+[1, 1][0]/2.0, 0]],
    ori: 0.0, pos: [106, (- 106)],
    lineWidth: 2.0, lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: undefined, depth: -16, interpolate: true,
  });
  
  resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  
          // add-on: list(s: string): string[]
          function list(s) {
              // if s is a string, we return a list of its characters
              if (typeof s === 'string')
                  return s.split('');
              else
                  // otherwise we return s:
                  return s;
          }
  
          block_num = 0;
  circle_vertices = [];
  theta = [];
  x = [];
  y = [];
  green = [(- 1), 0, (- 1)];
  red = [1, 0, 0];
  for (var i, _pj_c = 0, _pj_a = util.range(100), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
      i = _pj_a[_pj_c];
      theta = (((2 * pi) * i) / 99);
      x = (25 * Math.cos(theta));
      y = (25 * Math.sin(theta));
      circle_vertices.push([x, y]);
  }
  a = 21;
  diamond_vertices = [[(- a), a], [a, a], [a, (- a)], [(- a), (- a)]];
  b = 15;
  hori_start = [(- b), 0];
  hori_end = [b, 0];
  vert_start = [0, (- b)];
  vert_end = [0, b];
  c = 150;
  d = 106;
  loc1 = [c, 0];
  loc2 = [d, d];
  loc3 = [0, c];
  loc4 = [(- d), d];
  loc5 = [(- c), 0];
  loc6 = [(- d), (- d)];
  loc7 = [0, (- c)];
  loc8 = [d, (- d)];
  locs = [loc1, loc2, loc3, loc4, loc5, loc6, loc7, loc8];
  high_prob_loc = locs[Number.parseInt((Math.random() * 8))];
  low_prob_locs = function () {
      var _pj_a = [], _pj_b = locs;
      for (var _pj_c = 0, _pj_d = _pj_b.length; (_pj_c < _pj_d); _pj_c += 1) {
          var loc = _pj_b[_pj_c];
          if ((loc !== high_prob_loc)) {
              _pj_a.push(loc);
          }
      }
      return _pj_a;
  }
  .call(this);
  distractor_locs = [];
  tar_only_locs = [];
  for (var _, _pj_c = 0, _pj_a = util.range(32), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
      _ = _pj_a[_pj_c];
      distractor_locs.push(high_prob_loc);
  }
  for (var loc, _pj_c = 0, _pj_a = low_prob_locs, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
      loc = _pj_a[_pj_c];
      for (var _, _pj_f = 0, _pj_d = util.range(8), _pj_e = _pj_d.length; (_pj_f < _pj_e); _pj_f += 1) {
          _ = _pj_d[_pj_f];
          distractor_locs.push(loc);
      }
  }
  util.shuffle(distractor_locs);
  for (var _, _pj_c = 0, _pj_a = util.range(5), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
      _ = _pj_a[_pj_c];
      for (var loc, _pj_f = 0, _pj_d = locs, _pj_e = _pj_d.length; (_pj_f < _pj_e); _pj_f += 1) {
          loc = _pj_d[_pj_f];
          tar_only_locs.push(loc);
      }
  }
  util.shuffle(tar_only_locs);
  console.log(tar_only_locs);
  console.log(distractor_locs);
  shape = ["circle", "diamond"];
  distractor = ["red", "green", "no_dis"];
  distractor_new = ["red", "green"];
  detection = ["hori", "vert"];
  base_trial_count = ((shape.length * distractor.length) * detection.length);
  repeat_times = 10;
  trial_list_new = [];
  trial = [];
  for (var _, _pj_c = 0, _pj_a = util.range(repeat_times), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
      _ = _pj_a[_pj_c];
      for (var s, _pj_f = 0, _pj_d = shape, _pj_e = _pj_d.length; (_pj_f < _pj_e); _pj_f += 1) {
          s = _pj_d[_pj_f];
          for (var ds, _pj_i = 0, _pj_g = distractor, _pj_h = _pj_g.length; (_pj_i < _pj_h); _pj_i += 1) {
              ds = _pj_g[_pj_i];
              for (var d, _pj_l = 0, _pj_j = detection, _pj_k = _pj_j.length; (_pj_l < _pj_k); _pj_l += 1) {
                  d = _pj_j[_pj_l];
                  trial = [s, ds, d, ((d === "hori") ? "left" : "up")];
                  trial_list_new.push(trial);
              }
          }
      }
  }
  for (var s, _pj_c = 0, _pj_a = shape, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
      s = _pj_a[_pj_c];
      for (var ds, _pj_f = 0, _pj_d = distractor_new, _pj_e = _pj_d.length; (_pj_f < _pj_e); _pj_f += 1) {
          ds = _pj_d[_pj_f];
          for (var d, _pj_i = 0, _pj_g = detection, _pj_h = _pj_g.length; (_pj_i < _pj_h); _pj_i += 1) {
              d = _pj_g[_pj_i];
              trial = [s, ds, d, ((d === "hori") ? "left" : "up")];
              trial_list_new.push(trial);
          }
      }
  }
  util.shuffle(trial_list_new);
  j = 0;
  k = 0;
  filtered_locs = [];
  n = [];
  random_index = [];
  tar_both_loc = [];
  new_trial = [];
  dis_loc_fake = [9999, 9999];
  for (var i, _pj_c = 0, _pj_a = util.range(128), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
      i = _pj_a[_pj_c];
      new_trial = [];
      if ((trial_list_new[i][1].toString() === "no_dis")) {
          new_trial = [trial_list_new[i][0].toString(), trial_list_new[i][1].toString(), trial_list_new[i][2].toString(), trial_list_new[i][3].toString(), list([99999, 99999]), list(tar_only_locs[k])];
          trial_list_new[i] = new_trial;
          k = (k + 1);
      } else {
          filtered_locs = [];
          for (var m, _pj_f = 0, _pj_d = locs, _pj_e = _pj_d.length; (_pj_f < _pj_e); _pj_f += 1) {
              m = _pj_d[_pj_f];
              if ((m !== distractor_locs[j])) {
                  filtered_locs.push(m);
              }
          }
          n = filtered_locs.length;
          random_index = Number.parseInt((Math.random() * n));
          tar_both_loc = filtered_locs[random_index];
          new_trial = [trial_list_new[i][0].toString(), trial_list_new[i][1].toString(), trial_list_new[i][2].toString(), trial_list_new[i][3].toString(), list(distractor_locs[j]), list(tar_both_loc)];
          trial_list_new[i] = new_trial;
          j = (j + 1);
      }
  }
  util.shuffle(trial_list_new);
  current_trial = 0;
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 30.0,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "iti"
  itiClock = new util.Clock();
  iti_blank = new visual.TextStim({
    win: psychoJS.window,
    name: 'iti_blank',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 30.0,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "formal_cue"
  formal_cueClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '练习结束，请按空格开始实验\n\n再次提示，任务为找到独特形状\n（例如圆形中的菱形，或菱形中的圆形）\n\n并判断内部线段朝向',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 30.0,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "break_3"
  break_3Clock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: '现在可以休息\n\n准备好了按空格键继续',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 30.0,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "end"
  endClock = new util.Clock();
  end_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'end_2',
    text: '实验结束，谢谢参与',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 30.0,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _key_resp_allKeys;
var instrComponents;
function instrRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'instr'-------
    t = 0;
    instrClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    instrComponents = [];
    instrComponents.push(text);
    instrComponents.push(key_resp);
    
    instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instrRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'instr'-------
    // get current time
    t = instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instrRoutineEnd() {
  return async function () {
    //------Ending Routine 'instr'-------
    instrComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var trials;
var currentLoop;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 10, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials.forEach(function() {
      const snapshot = trials.getSnapshot();
    
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(fixRoutineBegin(snapshot));
      trialsLoopScheduler.add(fixRoutineEachFrame());
      trialsLoopScheduler.add(fixRoutineEnd());
      trialsLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsLoopScheduler.add(trialRoutineEachFrame());
      trialsLoopScheduler.add(trialRoutineEnd());
      trialsLoopScheduler.add(feedbackRoutineBegin(snapshot));
      trialsLoopScheduler.add(feedbackRoutineEachFrame());
      trialsLoopScheduler.add(feedbackRoutineEnd());
      trialsLoopScheduler.add(itiRoutineBegin(snapshot));
      trialsLoopScheduler.add(itiRoutineEachFrame());
      trialsLoopScheduler.add(itiRoutineEnd());
      trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


var trials_3;
function trials_3LoopBegin(trials_3LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_3 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 6, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials_3'
    });
    psychoJS.experiment.addLoop(trials_3); // add the loop to the experiment
    currentLoop = trials_3;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_3.forEach(function() {
      const snapshot = trials_3.getSnapshot();
    
      trials_3LoopScheduler.add(importConditions(snapshot));
      const trials_2LoopScheduler = new Scheduler(psychoJS);
      trials_3LoopScheduler.add(trials_2LoopBegin(trials_2LoopScheduler, snapshot));
      trials_3LoopScheduler.add(trials_2LoopScheduler);
      trials_3LoopScheduler.add(trials_2LoopEnd);
      trials_3LoopScheduler.add(break_3RoutineBegin(snapshot));
      trials_3LoopScheduler.add(break_3RoutineEachFrame());
      trials_3LoopScheduler.add(break_3RoutineEnd());
      trials_3LoopScheduler.add(endLoopIteration(trials_3LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var trials_2;
function trials_2LoopBegin(trials_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 128, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials_2'
    });
    psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
    currentLoop = trials_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_2.forEach(function() {
      const snapshot = trials_2.getSnapshot();
    
      trials_2LoopScheduler.add(importConditions(snapshot));
      trials_2LoopScheduler.add(fixRoutineBegin(snapshot));
      trials_2LoopScheduler.add(fixRoutineEachFrame());
      trials_2LoopScheduler.add(fixRoutineEnd());
      trials_2LoopScheduler.add(trialRoutineBegin(snapshot));
      trials_2LoopScheduler.add(trialRoutineEachFrame());
      trials_2LoopScheduler.add(trialRoutineEnd());
      trials_2LoopScheduler.add(feedbackRoutineBegin(snapshot));
      trials_2LoopScheduler.add(feedbackRoutineEachFrame());
      trials_2LoopScheduler.add(feedbackRoutineEnd());
      trials_2LoopScheduler.add(itiRoutineBegin(snapshot));
      trials_2LoopScheduler.add(itiRoutineEachFrame());
      trials_2LoopScheduler.add(itiRoutineEnd());
      trials_2LoopScheduler.add(endLoopIteration(trials_2LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_2LoopEnd() {
  psychoJS.experiment.removeLoop(trials_2);

  return Scheduler.Event.NEXT;
}


async function trials_3LoopEnd() {
  psychoJS.experiment.removeLoop(trials_3);

  return Scheduler.Event.NEXT;
}


var fixComponents;
function fixRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'fix'-------
    t = 0;
    fixClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    // keep track of which components have finished
    fixComponents = [];
    fixComponents.push(fix_circle);
    
    fixComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function fixRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'fix'-------
    // get current time
    t = fixClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fix_circle* updates
    if (t >= 0.0 && fix_circle.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix_circle.tStart = t;  // (not accounting for frame time here)
      fix_circle.frameNStart = frameN;  // exact frame index
      
      fix_circle.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fix_circle.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fix_circle.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    fixComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixRoutineEnd() {
  return async function () {
    //------Ending Routine 'fix'-------
    fixComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _resp_allKeys;
var trial_info;
var tar_shape;
var dis_color_condi;
var tar_line;
var cor_resp;
var dis_loc;
var tar_loc;
var shapes;
var lines;
var loc_to_shape_name;
var shape_map;
var colors;
var other_shape;
var other_color;
var loc;
var shape_name;
var line;
var line_dir;
var dis_line;
var feedback_text;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'trial'-------
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    loc1_shape.setLineColor(new util.Color('red'));
    resp.keys = undefined;
    resp.rt = undefined;
    _resp_allKeys = [];
    trial_info = trial_list_new[current_trial];
    current_trial = (current_trial + 1);
    psychoJS.experiment.addData("trial_para", trial_info);
    tar_shape = [];
    dis_color_condi = [];
    tar_line = [];
    cor_resp = [];
    dis_loc = [];
    tar_loc = [];
    tar_shape = trial_info[0];
    dis_color_condi = trial_info[1];
    tar_line = trial_info[2];
    cor_resp = trial_info[3];
    dis_loc = trial_info[4];
    tar_loc = trial_info[5];
    psychoJS.experiment.addData("tar_shape", tar_shape);
    psychoJS.experiment.addData("dis_color_condi", dis_color_condi);
    psychoJS.experiment.addData("tar_line", tar_line);
    psychoJS.experiment.addData("cor_resp", cor_resp);
    psychoJS.experiment.addData("dis_loc", dis_loc);
    psychoJS.experiment.addData("tar_loc", tar_loc);
    shapes = {"loc1_shape": loc1_shape, "loc2_shape": loc2_shape, "loc3_shape": loc3_shape, "loc4_shape": loc4_shape, "loc5_shape": loc5_shape, "loc6_shape": loc6_shape, "loc7_shape": loc7_shape, "loc8_shape": loc8_shape};
    lines = {"loc1_shape": loc1_line, "loc2_shape": loc2_line, "loc3_shape": loc3_line, "loc4_shape": loc4_line, "loc5_shape": loc5_line, "loc6_shape": loc6_line, "loc7_shape": loc7_line, "loc8_shape": loc8_line};
    loc_to_shape_name = {[[150, 0]]: "loc1_shape", [[106, 106]]: "loc2_shape", [[0, 150]]: "loc3_shape", [[(- 106), 106]]: "loc4_shape", [[(- 150), 0]]: "loc5_shape", [[(- 106), (- 106)]]: "loc6_shape", [[0, (- 150)]]: "loc7_shape", [[106, (- 106)]]: "loc8_shape"};
    shape_map = {"circle": circle_vertices, "diamond": diamond_vertices};
    colors = [];
    other_shape = ((tar_shape === "circle") ? "diamond" : "circle");
    if ((dis_color_condi === "red")) {
        other_color = green;
    } else {
        if ((dis_color_condi === "green")) {
            other_color = red;
        } else {
            if ((dis_color_condi === "no_dis")) {
                colors = [red, green];
                other_color = colors[Number.parseInt((Math.random() * colors.length))];
            }
        }
    }
    util.shuffle(locs);
    loc = [];
    shape_name = [];
    shape = [];
    line = [];
    line_dir = [];
    dis_line = [];
    for (var i, _pj_c = 0, _pj_a = util.range(locs.length), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        i = _pj_a[_pj_c];
        loc = locs[i];
        shape_name = loc_to_shape_name[loc];
        shape = shapes[shape_name];
        line = lines[shape_name];
        if ((loc === tar_loc)) {
            shape.vertices = shape_map[tar_shape];
            shape.lineColor = other_color;
            line.vertices = ((tar_line === "hori") ? [hori_start, hori_end] : [vert_start, vert_end]);
        } else {
            if ((loc === dis_loc)) {
                shape.vertices = shape_map[other_shape];
                shape.lineColor = ((dis_color_condi === "red") ? red : green);
                dis_line = [];
                line_dir = ["hori", "vert"];
                dis_line = line_dir[Number.parseInt((Math.random() * line_dir.length))];
                line.vertices = ((dis_line === "hori") ? [hori_start, hori_end] : [vert_start, vert_end]);
            } else {
                shape.vertices = shape_map[other_shape];
                shape.lineColor = other_color;
                if (((i % 2) === 0)) {
                    line.vertices = [hori_start, hori_end];
                } else {
                    line.vertices = [vert_start, vert_end];
                }
            }
        }
    }
    feedback_text = "";
    
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(fixation);
    trialComponents.push(loc1_shape);
    trialComponents.push(loc1_line);
    trialComponents.push(loc2_shape);
    trialComponents.push(loc2_line);
    trialComponents.push(loc3_shape);
    trialComponents.push(loc3_line);
    trialComponents.push(loc4_shape);
    trialComponents.push(loc4_line);
    trialComponents.push(loc5_shape);
    trialComponents.push(loc5_line);
    trialComponents.push(loc6_shape);
    trialComponents.push(loc6_line);
    trialComponents.push(loc7_shape);
    trialComponents.push(loc7_line);
    trialComponents.push(loc8_shape);
    trialComponents.push(loc8_line);
    trialComponents.push(resp);
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'trial'-------
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation* updates
    if (t >= 0.0 && fixation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation.tStart = t;  // (not accounting for frame time here)
      fixation.frameNStart = frameN;  // exact frame index
      
      fixation.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation.setAutoDraw(false);
    }
    
    // *loc1_shape* updates
    if (t >= 0.0 && loc1_shape.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      loc1_shape.tStart = t;  // (not accounting for frame time here)
      loc1_shape.frameNStart = frameN;  // exact frame index
      
      loc1_shape.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (loc1_shape.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      loc1_shape.setAutoDraw(false);
    }
    
    // *loc1_line* updates
    if (t >= 0.0 && loc1_line.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      loc1_line.tStart = t;  // (not accounting for frame time here)
      loc1_line.frameNStart = frameN;  // exact frame index
      
      loc1_line.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (loc1_line.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      loc1_line.setAutoDraw(false);
    }
    
    // *loc2_shape* updates
    if (t >= 0.0 && loc2_shape.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      loc2_shape.tStart = t;  // (not accounting for frame time here)
      loc2_shape.frameNStart = frameN;  // exact frame index
      
      loc2_shape.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (loc2_shape.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      loc2_shape.setAutoDraw(false);
    }
    
    // *loc2_line* updates
    if (t >= 0.0 && loc2_line.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      loc2_line.tStart = t;  // (not accounting for frame time here)
      loc2_line.frameNStart = frameN;  // exact frame index
      
      loc2_line.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (loc2_line.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      loc2_line.setAutoDraw(false);
    }
    
    // *loc3_shape* updates
    if (t >= 0.0 && loc3_shape.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      loc3_shape.tStart = t;  // (not accounting for frame time here)
      loc3_shape.frameNStart = frameN;  // exact frame index
      
      loc3_shape.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (loc3_shape.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      loc3_shape.setAutoDraw(false);
    }
    
    // *loc3_line* updates
    if (t >= 0.0 && loc3_line.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      loc3_line.tStart = t;  // (not accounting for frame time here)
      loc3_line.frameNStart = frameN;  // exact frame index
      
      loc3_line.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (loc3_line.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      loc3_line.setAutoDraw(false);
    }
    
    // *loc4_shape* updates
    if (t >= 0.0 && loc4_shape.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      loc4_shape.tStart = t;  // (not accounting for frame time here)
      loc4_shape.frameNStart = frameN;  // exact frame index
      
      loc4_shape.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (loc4_shape.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      loc4_shape.setAutoDraw(false);
    }
    
    // *loc4_line* updates
    if (t >= 0.0 && loc4_line.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      loc4_line.tStart = t;  // (not accounting for frame time here)
      loc4_line.frameNStart = frameN;  // exact frame index
      
      loc4_line.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (loc4_line.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      loc4_line.setAutoDraw(false);
    }
    
    // *loc5_shape* updates
    if (t >= 0.0 && loc5_shape.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      loc5_shape.tStart = t;  // (not accounting for frame time here)
      loc5_shape.frameNStart = frameN;  // exact frame index
      
      loc5_shape.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (loc5_shape.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      loc5_shape.setAutoDraw(false);
    }
    
    // *loc5_line* updates
    if (t >= 0.0 && loc5_line.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      loc5_line.tStart = t;  // (not accounting for frame time here)
      loc5_line.frameNStart = frameN;  // exact frame index
      
      loc5_line.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (loc5_line.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      loc5_line.setAutoDraw(false);
    }
    
    // *loc6_shape* updates
    if (t >= 0.0 && loc6_shape.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      loc6_shape.tStart = t;  // (not accounting for frame time here)
      loc6_shape.frameNStart = frameN;  // exact frame index
      
      loc6_shape.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (loc6_shape.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      loc6_shape.setAutoDraw(false);
    }
    
    // *loc6_line* updates
    if (t >= 0.0 && loc6_line.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      loc6_line.tStart = t;  // (not accounting for frame time here)
      loc6_line.frameNStart = frameN;  // exact frame index
      
      loc6_line.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (loc6_line.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      loc6_line.setAutoDraw(false);
    }
    
    // *loc7_shape* updates
    if (t >= 0.0 && loc7_shape.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      loc7_shape.tStart = t;  // (not accounting for frame time here)
      loc7_shape.frameNStart = frameN;  // exact frame index
      
      loc7_shape.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (loc7_shape.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      loc7_shape.setAutoDraw(false);
    }
    
    // *loc7_line* updates
    if (t >= 0.0 && loc7_line.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      loc7_line.tStart = t;  // (not accounting for frame time here)
      loc7_line.frameNStart = frameN;  // exact frame index
      
      loc7_line.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (loc7_line.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      loc7_line.setAutoDraw(false);
    }
    
    // *loc8_shape* updates
    if (t >= 0.0 && loc8_shape.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      loc8_shape.tStart = t;  // (not accounting for frame time here)
      loc8_shape.frameNStart = frameN;  // exact frame index
      
      loc8_shape.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (loc8_shape.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      loc8_shape.setAutoDraw(false);
    }
    
    // *loc8_line* updates
    if (t >= 0.0 && loc8_line.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      loc8_line.tStart = t;  // (not accounting for frame time here)
      loc8_line.frameNStart = frameN;  // exact frame index
      
      loc8_line.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (loc8_line.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      loc8_line.setAutoDraw(false);
    }
    
    // *resp* updates
    if (t >= 0.0 && resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp.tStart = t;  // (not accounting for frame time here)
      resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp.clearEvents(); });
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      resp.status = PsychoJS.Status.FINISHED;
  }

    if (resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp.getKeys({keyList: ['up', 'left'], waitRelease: false});
      _resp_allKeys = _resp_allKeys.concat(theseKeys);
      if (_resp_allKeys.length > 0) {
        resp.keys = _resp_allKeys[_resp_allKeys.length - 1].name;  // just the last key pressed
        resp.rt = _resp_allKeys[_resp_allKeys.length - 1].rt;
        // was this correct?
        if (resp.keys == cor_resp) {
            resp.corr = 1;
        } else {
            resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd() {
  return async function () {
    //------Ending Routine 'trial'-------
    trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (resp.keys === undefined) {
      if (['None','none',undefined].includes(cor_resp)) {
         resp.corr = 1;  // correct non-response
      } else {
         resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('resp.keys', resp.keys);
    psychoJS.experiment.addData('resp.corr', resp.corr);
    if (typeof resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp.rt', resp.rt);
        routineTimer.reset();
        }
    
    resp.stop();
    if ((resp.keys === null)) {
        feedback_text = "\u8bf7\u53ca\u65f6\u53cd\u5e94\uff0c\u96c6\u4e2d\u6ce8\u610f\u529b\uff01";
    } else {
        if ((resp.keys !== cor_resp)) {
            feedback_text = "\u9519\u8bef\uff01";
        } else {
            feedback_text = "";
        }
    }
    
    return Scheduler.Event.NEXT;
  };
}


var feedbackComponents;
function feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'feedback'-------
    t = 0;
    feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    text_4.setText(feedback_text);
    if ((feedback_text === "")) {
        continueRoutine = false;
    }
    
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(text_4);
    
    feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function feedbackRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'feedback'-------
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_4.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedbackRoutineEnd() {
  return async function () {
    //------Ending Routine 'feedback'-------
    feedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var itiComponents;
function itiRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'iti'-------
    t = 0;
    itiClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    iti_blank.setText(' ');
    // keep track of which components have finished
    itiComponents = [];
    itiComponents.push(iti_blank);
    
    itiComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function itiRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'iti'-------
    // get current time
    t = itiClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *iti_blank* updates
    if (t >= 0.0 && iti_blank.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      iti_blank.tStart = t;  // (not accounting for frame time here)
      iti_blank.frameNStart = frameN;  // exact frame index
      
      iti_blank.setAutoDraw(true);
    }

    frameRemains = 0.0 + (0.5 + (Math.random() * 0.25)) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (iti_blank.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      iti_blank.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    itiComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function itiRoutineEnd() {
  return async function () {
    //------Ending Routine 'iti'-------
    itiComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "iti" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_2_allKeys;
var formal_cueComponents;
function formal_cueRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'formal_cue'-------
    t = 0;
    formal_cueClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    current_trial = 0;
    
    // keep track of which components have finished
    formal_cueComponents = [];
    formal_cueComponents.push(text_2);
    formal_cueComponents.push(key_resp_2);
    
    formal_cueComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function formal_cueRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'formal_cue'-------
    // get current time
    t = formal_cueClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    formal_cueComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function formal_cueRoutineEnd() {
  return async function () {
    //------Ending Routine 'formal_cue'-------
    formal_cueComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "formal_cue" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_3_allKeys;
var break_3Components;
function break_3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'break_3'-------
    t = 0;
    break_3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    current_trial = 0;
    util.shuffle(trial_list_new);
    block_num = (block_num + 1);
    if ((block_num === 6)) {
        continueRoutine = false;
    }
    psychoJS.experiment.addData("block_num", block_num);
    
    // keep track of which components have finished
    break_3Components = [];
    break_3Components.push(text_3);
    break_3Components.push(key_resp_3);
    
    break_3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function break_3RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'break_3'-------
    // get current time
    t = break_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }

    
    // *key_resp_3* updates
    if (t >= 0.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    break_3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function break_3RoutineEnd() {
  return async function () {
    //------Ending Routine 'break_3'-------
    break_3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    // the Routine "break_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var endComponents;
function endRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'end'-------
    t = 0;
    endClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    endComponents = [];
    endComponents.push(end_2);
    
    endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function endRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'end'-------
    // get current time
    t = endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *end_2* updates
    if (t >= 0.0 && end_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_2.tStart = t;  // (not accounting for frame time here)
      end_2.frameNStart = frameN;  // exact frame index
      
      end_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (end_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      end_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endRoutineEnd() {
  return async function () {
    //------Ending Routine 'end'-------
    endComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
