package None;

/* metamodel_version: 1.11.0 */
/* version: 1.1-rc2 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  FIXML generator hints carried inside <fixr:appinfo purpose="FIXML">. Captures whether a component is inlined in its containing message and whether an element is ignored by the FIXML generator.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class FIXMLencodingType  {

  private Boolean inlined;
  private Boolean notReqXml;


}