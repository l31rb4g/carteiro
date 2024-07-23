
function showMailList() {
    $('mail').setStyle('display', 'none');
    $('mail_list').setStyle('display', 'block');
    $$('#toolbar .mail_list').setStyle('display', 'flex');
    $$('#toolbar .mail').setStyle('display', 'none');
}

function showMail(li) {
    li.addClass('read');
    $$('#toolbar .mail_list').setStyle('display', 'none');
    $$('#toolbar .mail').setStyle('display', 'block');
    $('mail_list').setStyle('display', 'none');
    $('mail').setStyle('display', 'block');
    $$('#mail .id').set('html', li.getElement('.id').get('html'));
    $$('#mail .subject').set('html', li.getElement('.subject').get('html'));
    $$('#mail .from').set('html', li.getElement('.from_full').get('html'));
    $$('#mail .to').set('html', li.getElement('.to').get('html'));
    $$('#mail .content').set('html', li.getElement('.content_full').get('html'));
    $$('#mail .data').set('html', li.getElement('.data_full').get('html'));

    const pk = li.getElement('.id').get('text').toInt();
    new Request({
        url: '/read',
        data: {
            id: pk,
        },
    }).send();
}

window.addEvent('domready', () => {
    $('btn_reload').addEvent('click', () => {
        window.location.reload();
    });
    $('btn_back').addEvent('click', () => {
        showMailList();
    });

    $('btn_delete').addEvent('click', () => {
        const pk = $$('#mail .id')[0].get('text').toInt();
        new Request({
            url: '/delete',
            data: {
                id: pk,
            },
        }).send();
        $('mail_' + pk).destroy();
        showMailList();
    });

    $$('#mail_list li').each((li) => {
        li.addEvent('click', (ev) => {
            if (ev.target.tagName === 'INPUT') return;
            showMail(li);
        });
    });
});
