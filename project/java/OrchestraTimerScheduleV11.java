package example;

/* metamodel_version: 1.12.0 */
/* version: 1.0, 1.1-rc3 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A step that starts, stops or restarts an actor's timer, with its interval and what to do when it runs out.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraTimerScheduleV11  {

  private OrchestraActionV11 fixrActivity;
  private String fixrActor;
  private String fixrName;
  private String fixrOperation;
  private String fixrInterval;


}