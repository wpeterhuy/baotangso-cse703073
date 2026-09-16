<?php
namespace App\Models;
use Illuminate\Database\Eloquent\Model;

class Tour extends Model
{
    protected $table = 'tours';
    const UPDATED_AT = null;
    protected $fillable = ['museum_id','title','slug','theme','description','duration_minutes','cover_image','status'];
    public function museum() { return $this->belongsTo(Museum::class); }
    public function steps() { return $this->hasMany(TourStep::class)->orderBy('step_no'); }
    public function visitSessions() { return $this->hasMany(VisitSession::class); }
}
