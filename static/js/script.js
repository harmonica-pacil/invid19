const notify = document.querySelector('#notify');
const notifyTypeAttr = notify.getAttribute('notifyType');
const notifyMessageAttr = notify.getAttribute('notifyMessage');

let notifyType = 'success';
switch (notifyTypeAttr) {
  case 'error':
    notifyType = 'danger';
    break;
  case 'info':
    notifyType = 'warning';
    break;
  default:
    notifyType = 'success';
    break;
}

Notify({
  title: notifyMessageAttr,
  type: notifyType,
  duration: 3000,
  position: 'top center',
});
