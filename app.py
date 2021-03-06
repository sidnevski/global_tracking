from flask import Flask, render_template
import scripts.qr_driver
import scripts.afkl_driver
import scripts.lh_driver
import scripts.data

app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'index.html'
    )

@app.route('/trackship')
def trackship(track_shipment_id='shipment_id_1'):
    tracking_ids = scripts.data.get_tracking_ids(track_shipment_id)

    track_request_qr = tracking_ids['qr']
    track_request_afkl = tracking_ids['afkl']
    track_request_lh = tracking_ids['lh']
    
    track_response_qr = scripts.qr_driver.track_shipment(
        track_request_qr
    )

    track_response_afkl = scripts.afkl_driver.track_shipment(
        track_request_afkl
    )

    track_response_lh = scripts.lh_driver.track_lh_shipment(
        track_request_lh
    )
    
    return render_template(
        'trackship.html',
        track_response_qr=track_response_qr,
        track_response_afkl=track_response_afkl,
        track_response_lh=track_response_lh
    )

@app.route('/confirmed')
def track(track_shipment_id='shipment_id_1'):
    tracking_ids = scripts.data.get_tracking_ids(track_shipment_id)

    track_request_qr = tracking_ids['qr']
    track_request_afkl = tracking_ids['afkl']
    track_request_lh = tracking_ids['lh']
    
    track_response_qr = scripts.qr_driver.track_shipment(
        track_request_qr
    )

    track_response_afkl = scripts.afkl_driver.track_shipment(
        track_request_afkl
    )

    track_response_lh = scripts.lh_driver.track_lh_shipment(
        track_request_lh
    )
    
    return render_template(
        'confirmed.html',
        track_response_qr=track_response_qr,
        track_response_afkl=track_response_afkl,
        track_response_lh=track_response_lh
    )

@app.route('/transit')
def transit(track_shipment_id='shipment_id_1'):
    tracking_ids = scripts.data.get_tracking_ids(track_shipment_id)

    track_request_qr = tracking_ids['qr']
    track_request_afkl = tracking_ids['afkl']
    track_request_lh = tracking_ids['lh']
    
    track_response_qr = scripts.qr_driver.track_shipment(
        track_request_qr
    )

    track_response_afkl = scripts.afkl_driver.track_shipment(
        track_request_afkl
    )

    track_response_lh = scripts.lh_driver.track_lh_shipment(
        track_request_lh
    )
    
    return render_template(
        'transit.html',
        track_response_qr=track_response_qr,
        track_response_afkl=track_response_afkl,
        track_response_lh=track_response_lh
    )

@app.route('/delivered')
def delivered(track_shipment_id='shipment_id_1'):
    tracking_ids = scripts.data.get_tracking_ids(track_shipment_id)

    track_request_qr = tracking_ids['qr']
    track_request_afkl = tracking_ids['afkl']
    track_request_lh = tracking_ids['lh']
    
    track_response_qr = scripts.qr_driver.track_shipment(
        track_request_qr
    )

    track_response_afkl = scripts.afkl_driver.track_shipment(
        track_request_afkl
    )

    track_response_lh = scripts.lh_driver.track_lh_shipment(
        track_request_lh
    )
    
    return render_template(
        'delivered.html',
        track_response_qr=track_response_qr,
        track_response_afkl=track_response_afkl,
        track_response_lh=track_response_lh
    )

@app.errorhandler(500)
def timeout(e):
    return render_template(
        '500.html'
)

if __name__ == '__main__':
    app.run(debug=True)